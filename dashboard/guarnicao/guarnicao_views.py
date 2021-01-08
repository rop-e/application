from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import (
    JsonResponse,
    FileResponse
)
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from utils.gerar_pdf import GerarPDF
import json
from ropd.settings import MEDIA_URL

# MODELS
from guarnicao.models import (
    Guarnicao,
    GuarnicaoAIT,
    GuarnicaoRRD,
    GuarnicaoTRAV,
    Companhia
)
from opo.models import OPORelatorio
from policial.models import Policial
from ocorrencia.models import Ocorrencia
from policialviatura.models import PolicialViatura
from rat.models import RAT
from endereco.models import Municipios

# SERIALIZER
from policialviatura.serializers import ListPolicialViaturaSerializer
from ocorrencia.serializers import ListOcorrenciaSerializer
from guarnicao.serializers import (
    GuarnicaoAITSerializer,
    GuarnicaoRRDSerializer,
    GuarnicaoTRAVSerializer,
    ListGuarnicaoAITSerializer,
    ListGuarnicaoRRDSerializer,
    ListGuarnicaoTRAVSerializer
)
from rat.serializers import ListRATSerializer

# VIEWS
from dashboard.policialviatura.policialviatura_views import (
    listar_policiais_na_viatura
)
from django.http import QueryDict

# FORMS
from dashboard.guarnicao.forms import (
    FormGuarnicao,
    FormGuarnicaoAIT,
    FormGuarnicaoRRD,
    FormGuarnicaoTRAV,
    FormCompanhia
)
from dashboard.observacao.forms import FormObservacao
from dashboard.policialviatura.forms import FormPolicialViatura

STATUS_GUARNICAO = (
    ("andamento", "EM ANDAMENTO"),
    ("encerrada", "ENCERRADA")
)

# PDF
from ropd.settings import (
    MEDIA_URL,
    PDF_ROOT
)
from pathlib import Path
import io
from reportlab.pdfgen import canvas


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Guarnicao.objects.all()
    status = request.GET.get("status", "")
    companhia = request.GET.get("companhia", "")
    municipio = request.GET.get("municipio", "")
    dataabertura = request.GET.get("data_abertura")
    datafechamento = request.GET.get("data_fechamento")
    bloqueadas = request.GET.get("bloqueadas", "")

    if is_valid_queryparam(status):
        if status == "andamento":
            qs = qs.filter(datafechamento__isnull=True)
        elif status == "encerrada":
            qs = qs.filter(datafechamento__isnull=False)

    if is_valid_queryparam(companhia):
        qs = qs.filter(companhia=companhia)

    if is_valid_queryparam(municipio):
        qs = qs.filter(municipio=municipio)
    
    if is_valid_queryparam(dataabertura):
        dabertura = timezone.now().strptime(dataabertura, "%d/%m/%Y")
        qs = qs.filter(dataabertura__date__gte=dabertura)

    if is_valid_queryparam(datafechamento):
        dfechamento = timezone.now().strptime(datafechamento, "%d/%m/%Y")
        qs = qs.filter(datafechamento__date__lte=dfechamento)

    if bloqueadas == "on":
        qs = qs.filter(ativo=False, datafechamento__isnull=True)

    return qs


@login_required
def listar_guarnicoes_todas(request):
    qs = filter(request)

    id_companhias = []

    for guarnicao in Guarnicao.objects.all():
        id_companhias.append(guarnicao.companhia.id)

    numero_pagina = request.GET.get("pagina", "")
    paginador = Paginator(qs.order_by("-id"), 10)

    filtros = QueryDict(mutable=True)
    checkbox = []

    for k, v in request.GET.items():
        if v != "":
            if k == "status":
                if v == "andamento":
                    v = "EM ANDAMENTO"
                elif v == "encerrada":
                    v = "ENCERRADA"

                filtros.appendlist("Status", v)
            elif k == "companhia":
                filtros.appendlist("Companhia", Companhia.objects.get(id=v))
            elif k == "data_abertura":
                filtros.appendlist("Data de abertura", v)
            elif k == "data_fechamento":
                filtros.appendlist("Data de fechamento", v)
            elif k == "bloqueadas":
                checkbox.append("Bloqueadas")

    context = {
        "guarnicoes": paginador.get_page(numero_pagina),
        "status": STATUS_GUARNICAO,
        "companhias": Companhia.objects.filter(id__in=id_companhias).distinct(),
        "filtros": filtros,
        "checkbox": checkbox
    }

    return render(request, "gestao/listar_guarnicoes_todas.html", context)


@login_required
def listar_guarnicoes_comandante(request):
    policial = request.user.policial.id

    paginador = Paginator(
                get_guarnicoes().filter(comandante=policial), 4)
    numero_pagina = request.GET.get("pagina")
    guarnicoes = paginador.get_page(numero_pagina)

    context = {
        "guarnicoes": guarnicoes,
        "guarnicao_ativa": get_guarnicao(policial)
    }

    return render(request, "gestao/listar_guarnicoes_comandante.html", context)


@login_required
def listar_guarnicoes_ativas(request):
    qs = filter(request).filter(datafechamento=None, ativo=True)

    id_companhias = []
    id_municipios = []

    for guarnicao in Guarnicao.objects.filter(datafechamento__isnull=True, ativo=True):
        id_companhias.append(guarnicao.companhia.id)
        id_municipios.append(guarnicao.municipio.codigo_ibge)

    numero_pagina = request.GET.get("pagina", "")
    paginador = Paginator(qs.order_by("-id"), 10)

    filtros = QueryDict(mutable=True)

    for k, v in request.GET.items():
        if v != "":
            if k == "companhia":
                filtros.appendlist("Companhia", Companhia.objects.get(id=v))
            elif k == "municipio":
                filtros.appendlist("Município atuante", Municipios.objects.get(codigo_ibge=v))

    context = {
        "guarnicoes": paginador.get_page(numero_pagina),
        "companhias": Companhia.objects.filter(id__in=id_companhias).distinct(),
        "municipios": Municipios.objects.filter(codigo_ibge__in=id_municipios).distinct(),
        "filtros": filtros,
    }

    return render(request, "gestao/listar_guarnicoes_ativas.html", context)


@login_required
def ajax_guarnicoes_ativas(request):
    if request.is_ajax:
        return JsonResponse({
            "ativas": Guarnicao.objects.filter(datafechamento=None, ativo=True).count()
        }, status=200)
    
    return JsonResponse({}, status=200)


@login_required
def visualizar_guarnicao(request, id):
    try:
        guarnicao = Guarnicao.objects.get(id=id)

        context = {
            "guarnicao": guarnicao,
            "observacao": FormObservacao()
        }

        return render(request, "gestao/visualizar_guarnicao.html", context)
    except Exception:
        return redirect("index")


@login_required
def adicionar_guarnicao(request):
    if not verifica_guarnicao_ativa(request.user.policial.id):
        context = {"guarnicao": FormGuarnicao(request)}

        return render(request, "gestao/adicionar_guarnicao.html", context)
    else:
        return redirect("guarnicao:listar_guarnicoes_comandante")


@login_required
@csrf_exempt
def post_delete_guarnicao(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("guarnicao")
            guarnicao = Guarnicao.objects.get(id=id)

            if guarnicao:
                guarnicao.delete()

            return JsonResponse({"redirect": reverse("index")}, status=200)
        except Exception as error:
            raise error


@login_required
def post_guarnicao(request):
    if not verifica_guarnicao_ativa(request.user.policial.id):
        if request.is_ajax and request.method == "POST":
            guarnicao = FormGuarnicao(request, request.POST or None)

            if guarnicao.is_valid():
                guarnicao = guarnicao.save(commit=False)
                guarnicao.comandante_id = request.user.policial.id
                guarnicao.save()
                
                # permuta = Permuta.objects.filter(policial_id=request.user.policial.id, guarnicao_nova__isnull=True)
                # if permuta:
                #     permuta.update(guarnicao_nova=guarnicao)

                return JsonResponse({
                    "redirect": reverse(
                        "guarnicao:adicionar_policial_guarnicao",
                        kwargs={"guarnicao": guarnicao.id})
                }, status=200)
            else:
                return JsonResponse(guarnicao.errors, status=400)
    else:
        return JsonResponse({
            "redirect": redirect("guarnicao:listar_guarnicoes_comandante")
        }, status=200)


@login_required
def get_policiais_guarnicao(request):
    id = request.GET.get("guarnicao", None)
    policialviatura = PolicialViatura.objects.filter(
        guarnicao=id).order_by("-id")

    data = dict()

    if policialviatura:
        serializer = ListPolicialViaturaSerializer(policialviatura, many=True)
        data["policialviatura"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def adicionar_policial_guarnicao(request, guarnicao):
    guarnicao = Guarnicao.objects.get(id=guarnicao)
    if guarnicao.ativo:
        if request.method == "POST":
            post_policial(request)

        context = {
            "guarnicao": guarnicao,
            "policiais": listar_policiais_na_viatura(guarnicao.id),
            "policialviatura": FormPolicialViatura()
        }

        return render(request, "gestao/adicionar_policial_guarnicao.html", context)
    else:
        return redirect("guarnicao:listar_guarnicoes_comandante")


@login_required
def post_policial(request):
    if request.is_ajax and request.method == "POST":
        policial = FormPolicialViatura(
                   request.POST or None)

        if policial.is_valid():
            policial = policial.save(commit=False)
        
            query = PolicialViatura.objects.filter(
                    guarnicao=policial.guarnicao)
            
            if query.filter(policial=policial.policial).exists():
                return JsonResponse({
                    "error": "Você já inseriu esse policial na guarnição!"
                }, status=400)

            if policial.viatura is not None:
                if query.filter(
                        viatura__isnull=True).exists():
                    return JsonResponse({
                        "error": "Você já inseriu policiais sem viatura"
                                 " na guarnição. Remova-os, ou deixe o"
                                 " o campo viatura deste policial em"
                                 " branco."
                    }, status=400)
                if policial.funcao.funcao != "MOTORISTA/PILOTO":
                    if not query.filter(
                            viatura=policial.viatura).exists():
                        return JsonResponse({
                            "error": "Informe primeiro o motorista/piloto"
                                     " da viatura!"
                        }, status=400)
                else:
                    if query.filter(
                            viatura=policial.viatura,
                            funcao__funcao="MOTORISTA/PILOTO").exists():
                        return JsonResponse({
                            "error": "Você já informou o motorista/piloto"
                                     " dessa viatura!"
                        }, status=400)

                if policial.kmsaida != "":
                    qset = PolicialViatura.objects.filter(
                            viatura=policial.viatura,
                            guarnicao=policial.guarnicao)
                    if qset.exclude(kmsaida='').exists():
                        pv = PolicialViatura.objects.get(
                            viatura=policial.viatura,
                            guarnicao=policial.guarnicao)
                        
                        saida = pv.kmsaida
                        volta = pv.kmvolta

                        if saida == volta:
                            return JsonResponse({
                                "error":
                                    f"Você já inseriu a quilometragem da viatura {policial.viatura}!"
                            }, status=400)
                    if qset.exists():
                        kmvoltaultima = qset.exclude(
                                kmvolta="").last()
                        if policial.kmsaida < kmvoltaultima.kmvolta:
                            return JsonResponse({
                                "error":
                                    "Quilometragem de saída da viatura menor"
                                    " que a última quilometragem de volta."
                            }, status=400)

                if policial.kmsaida == "":
                    if not query.filter(
                            viatura=policial.viatura).exists():
                        return JsonResponse({
                            "error": "Por favor, informe a"
                                     " quilometragem da viatura!"
                        }, status=400)
            else:
                if policial.funcao.funcao == "MOTORISTA/PILOTO":
                    if not query.filter(
                            viatura=policial.viatura,
                            funcao__funcao=policial.funcao.funcao).exists():
                        return JsonResponse({
                            "error": "Informe a viatura!"
                        }, status=400)
                if query.filter(
                        viatura__isnull=False).exists():
                    return JsonResponse({
                        "error": "Você já inseriu policiais em viaturas"
                                 " na guarnição. Remova-os, ou informe"
                                 " uma viatura para este policial."
                    }, status=400)

            policial.kmvolta = policial.kmsaida
            policial.save()

            # permuta = Permuta.objects.filter(policial=policial.policial, guarnicao_nova__isnull=True)
            # if permuta:
            #     permuta.update(guarnicao_nova=policial.guarnicao)

            instance = ListPolicialViaturaSerializer(policial).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse(policial.errors, status=400)

from guarnicao.models import Permuta

@login_required
@csrf_exempt
def permutar(request):
    policial = request.user.policial.id
    if PolicialViatura.objects.filter(policial=policial, ativo=True).last():
        policialviatura = PolicialViatura.objects.get(policial=policial, ativo=True)
        guarnicao = policialviatura.guarnicao

        if request.is_ajax and request.method == "POST":
            Permuta.objects.create(policial_id=policial, guarnicao_ultima=guarnicao)
            policialviatura.ativo = False
            policialviatura.save()

            return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=400)


@login_required
@csrf_exempt
def delete_policial(request):
    if request.is_ajax and request.method == "POST":
        data = dict()
        id = request.POST.get("id")
        policialviatura = PolicialViatura.objects.get(id=id)

        if policialviatura:
            policialviatura.delete()
            data["message"] = "Policial removido."
        else:
            data["message"] = "Erro!"

        return JsonResponse(data)


@login_required
def post_ait(request):
    if request.is_ajax and request.method == "POST":
        ait = FormGuarnicaoAIT(request.POST or None)

        if ait.is_valid():
            ait = ait.save()

            instance = GuarnicaoAITSerializer(ait).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse(ait.errors, status=400)


@login_required
def edit_ait(request, id):
    try:
        ait = GuarnicaoAIT.objects.get(id=id)

        context = {
            "id": ait.id,
            "ait": FormGuarnicaoAIT(instance=ait)
        }

        return render(request, "gestao/edits/edit_ait.html", context)
    except Exception:
        pass


@login_required
def post_edit_ait(request):
    if request.is_ajax and request.method == "POST":
        instance = GuarnicaoAIT.objects.get(id=request.POST.get("id_ait"))

        ait = FormGuarnicaoAIT(request.POST, instance=instance)

        if ait.is_valid():
            ait.save()

            return JsonResponse({"message": "AIT atualizado."}, status=200)
        else:
            return JsonResponse(ait.errors, status=400)


@login_required
@csrf_exempt
def delete_ait(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            ait = GuarnicaoAIT.objects.get(id=id)

            data = dict()

            if ait:
                ait.delete()
                data["message"] = "AIT removido."

            return JsonResponse(data)
        except Exception as error:
            raise error


@login_required
def post_rrd(request):
    if request.is_ajax and request.method == "POST":
        rrd = FormGuarnicaoRRD(request.POST or None)

        if rrd.is_valid():
            rrd = rrd.save()

            instance = GuarnicaoAITSerializer(rrd).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse(rrd.errors, status=400)


@login_required
def edit_rrd(request, id):
    try:
        rrd = GuarnicaoRRD.objects.get(id=id)

        context = {
            "id": rrd.id,
            "rrd": FormGuarnicaoRRD(instance=rrd)
        }

        return render(request, "gestao/edits/edit_rrd.html", context)
    except Exception:
        pass


@login_required
def post_edit_rrd(request):
    if request.is_ajax and request.method == "POST":
        instance = GuarnicaoRRD.objects.get(id=request.POST.get("id_rrd"))

        rrd = FormGuarnicaoRRD(request.POST, instance=instance)

        if rrd.is_valid():
            rrd.save()

            return JsonResponse({"message": "RRD atualizado."}, status=200)
        else:
            return JsonResponse(rrd.errors, status=400)


@login_required
@csrf_exempt
def delete_rrd(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            rrd = GuarnicaoRRD.objects.get(id=id)

            data = dict()

            if rrd:
                rrd.delete()
                data["message"] = "RRD removido."

            return JsonResponse(data)
        except Exception as error:
            raise error


@login_required
def post_trav(request):
    if request.is_ajax and request.method == "POST":
        trav = FormGuarnicaoTRAV(request.POST or None)

        if trav.is_valid():
            trav = trav.save()

            instance = GuarnicaoTRAVSerializer(trav).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse(trav.errors, status=400)


@login_required
def edit_trav(request, id):
    try:
        trav = GuarnicaoTRAV.objects.get(id=id)

        context = {
            "id": trav.id,
            "trav": FormGuarnicaoTRAV(instance=trav)
        }

        return render(request, "gestao/edits/edit_trav.html", context)
    except Exception:
        pass


@login_required
def post_edit_trav(request):
    if request.is_ajax and request.method == "POST":
        instance = GuarnicaoTRAV.objects.get(id=request.POST.get("id_trav"))

        trav = FormGuarnicaoTRAV(request.POST, instance=instance)

        if trav.is_valid():
            trav.save()

            return JsonResponse({"message": "TRAV atualizado."}, status=200)
        else:
            return JsonResponse(trav.errors, status=400)


@login_required
@csrf_exempt
def delete_trav(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            trav = GuarnicaoTRAV.objects.get(id=id)

            data = dict()

            if trav:
                trav.delete()
                data["message"] = "TRAV removido."

            return JsonResponse(data)
        except Exception as error:
            raise error


@login_required
def encerrar_guarnicao(request, guarnicao):
    if verifica_guarnicao_ativa(request.user.policial.id):
        guarnicao = Guarnicao.objects.get(id=guarnicao)

        if not guarnicao.datafechamento:
            opos = OPORelatorio.objects.filter(guarnicao=guarnicao)

            if request.method == "POST":
                post_ait(request)
                post_rrd(request)
                post_trav(request)

            context = {
                "guarnicao": guarnicao,
                "ait": FormGuarnicaoAIT(),
                "rrd": FormGuarnicaoRRD(),
                "trav": FormGuarnicaoTRAV(),
                "opos": opos
            }

            return render(request, "gestao/encerrar_guarnicao.html", context)

    return redirect("index")


@login_required
def verifica_guarnicao_bloqueada(request):
    if request.is_ajax:
        guarnicao = Guarnicao.objects.get(id=request.GET.get("guarnicao", None))

        data = dict()

        if not guarnicao.ativo:
            data["block"] = True

        return JsonResponse(data)


@login_required
def bloqueia_guarnicao(request):
    if request.is_ajax and request.method == "POST":
        guarnicao = Guarnicao.objects.get(id=request.POST.get("id_guarnicao", None))
        observacao = FormObservacao(request.POST or None)

        guarnicao.bloqueadopor = Policial.objects.get(id=request.user.policial.id)
        guarnicao.ativo = False

        if observacao.is_valid():
            guarnicao.observacao = observacao.save()

        guarnicao.save()

        PolicialViatura.objects.filter(guarnicao=guarnicao).update(ativo=False)

        return JsonResponse({}, status=200)


@login_required
def get_aits_guarnicao(request):
    if request.is_ajax and request.method == "GET":
        guarnicao = request.GET.get("guarnicao", None)

        ait = GuarnicaoAIT.objects.filter(guarnicao=guarnicao)

        data = dict()

        if ait:
            serializer = ListGuarnicaoAITSerializer(ait, many=True)
            data["aits"] = list(serializer.data)

        return JsonResponse(data)


@login_required
def get_rrds_guarnicao(request):
    if request.is_ajax and request.method == "GET":
        guarnicao = request.GET.get("guarnicao", None)

        rrd = GuarnicaoRRD.objects.filter(guarnicao=guarnicao)

        data = dict()
        
        if rrd:
            serializer = ListGuarnicaoRRDSerializer(rrd, many=True)
            data["rrds"] = list(serializer.data)

        return JsonResponse(data)


@login_required
def get_travs_guarnicao(request):
    if request.is_ajax and request.method == "GET":
        guarnicao = request.GET.get("guarnicao", None)

        trav = GuarnicaoTRAV.objects.filter(guarnicao=guarnicao)

        data = dict()

        if trav:
            serializer = ListGuarnicaoTRAVSerializer(trav, many=True)
            data["travs"] = list(serializer.data)

        return JsonResponse(data)


def ocorrencias_guarnicao(guarnicao):
    try:
        return Ocorrencia.objects.filter(guarnicao=guarnicao)
    except Exception:
        pass


@login_required
def get_ocorrencias_guarnicao(request):
    if request.is_ajax and request.method == "GET":
        guarnicao = request.GET.get("guarnicao", None)

        ocorrencias = Ocorrencia.objects.filter(guarnicao=guarnicao)

        data = dict()

        if ocorrencias:
            serializer = ListOcorrenciaSerializer(ocorrencias, many=True)
            data["ocorrencias"] = list(serializer.data)

        return JsonResponse(data)


@login_required
def get_rats_guarnicao(request):
    if request.is_ajax and request.method == "GET":
        guarnicao = request.GET.get("guarnicao", None)

        rats = RAT.objects.filter(guarnicao=guarnicao)

        data = dict()

        if rats:
            serializer = ListRATSerializer(rats, many=True)
            data["rats"] = list(serializer.data)

        return JsonResponse(data)


@login_required
def verifica_andamento(request):
    if request.is_ajax and request.method == "GET":
        guarnicao = Guarnicao.objects.get(id=request.GET.get("guarnicao", None))
        data = dict()

        ocorrencia = Ocorrencia.objects.filter(guarnicao=guarnicao, relatorio__isnull=True)
        opo = OPORelatorio.objects.filter(guarnicao=guarnicao, status="andamento")
        rat = RAT.objects.filter(guarnicao=guarnicao, relatorio__isnull=True)

        if ocorrencia:
            data["ocorrencia"] = True
        if opo:
            data["opo"] = True
        if rat:
            data["rat"] = True
        
        return JsonResponse(data, status=200)

    return JsonResponse({}, status=200)


@login_required
@csrf_exempt
def post_encerra_guarnicao(request):
    if request.is_ajax and request.method == "POST":
        guarnicao = Guarnicao.objects.get(id=request.POST.get("guarnicao"))
        relatorio = request.POST.get("relatorio")
        data = json.loads(request.POST.get("viaturas"))

        guarnicao.relatorio = relatorio
        guarnicao.datafechamento = timezone.now()
        guarnicao.save()

        for viatura in data:
            PolicialViatura.objects.filter(
                id=viatura["viatura"],
                guarnicao=guarnicao).update(kmvolta=viatura["kmvolta"])

        return JsonResponse({
            "pdf": reverse(
                "guarnicao:geraemostrapdfguarnicao",
                kwargs={"id": guarnicao.id}),
            "redirect": reverse("index")
        }, status=200)

from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def geraemostrapdfguarnicao(request, id):
    try:
        guarnicao = Guarnicao.objects.get(id=id)
        aits = GuarnicaoAIT.objects.filter(guarnicao=guarnicao)
        rrds = GuarnicaoRRD.objects.filter(guarnicao=guarnicao)
        travs = GuarnicaoTRAV.objects.filter(guarnicao=guarnicao)

        opos = OPORelatorio.objects.filter(guarnicao=guarnicao, status="finalizada")
        
        pasta = "guarnicoes/"
        nomearquivo = "Guarnicao_" + str(guarnicao.id) + "-" +\
            str(guarnicao.companhia) + "-Encerramento_de_Servico-" +\
            str(guarnicao.municipio.nome) + "_Data__" +\
            timezone.localtime(guarnicao.dataabertura).strftime("%d_%m_%Y")

        arquivo = pasta + str(nomearquivo + ".pdf").replace(" ", "_")
        
        filename = PDF_ROOT + pasta + str(nomearquivo + ".pdf").replace(" ", "_")

        my_file = Path(filename)

        if not my_file.is_file():
            context_pdf = {
                "guarnicao": guarnicao,
                "pms": PolicialViatura.objects.filter(
                    guarnicao=guarnicao).order_by("policial__nomeguerra"),
                "ocorrencias": ocorrencias_guarnicao(guarnicao),
                "rats": RAT.objects.filter(guarnicao=guarnicao),
                "aits": aits,
                "aitscarros": aits.filter(tipoveiculo="carro").count(),
                "aitsmotos": aits.filter(tipoveiculo="moto").count(),
                "rrds": rrds,
                "rrdscarros": rrds.filter(tipoveiculo="carro").count(),
                "rrdsmotos": rrds.filter(tipoveiculo="moto").count(),
                "travs": travs,
                "travscarros": travs.filter(tipoveiculo="carro").count(),
                "travsmotos": travs.filter(tipoveiculo="moto").count(),
                "opos": opos
            }

            GerarPDF("gestao/pdf.html", context_pdf, arquivo)

        with open(filename, 'r'):
            response = FileResponse(open(filename))
            return response

    except Exception as error:
        raise error


@login_required
def get_viaturas(request):
    if request.is_ajax and request.method == "GET":
        guarnicao = request.GET.get("guarnicao")

        data = dict()

        if PolicialViatura.objects.filter(
                guarnicao_id=guarnicao,
                viatura__isnull=True).count() > 0:
            data["viaturas"] = False
            return JsonResponse(data)
        else:
            policialviatura = PolicialViatura.objects.filter(
                guarnicao_id=guarnicao).order_by("-id")
            if policialviatura:
                serializer = ListPolicialViaturaSerializer(
                    policialviatura, many=True)
                data["viaturas"] = True
                data["policialviatura"] = list(serializer.data)

                return JsonResponse(data)
            else:
                data["viaturas"] = False
                return JsonResponse(data)


@login_required
def listar_companhias(request):
    paginador = Paginator(
                get_companhias(), 10)
    numero_pagina = request.GET.get("pagina")
    companhias = paginador.get_page(numero_pagina)

    context = {"companhias": companhias}

    return render(request, "gestao/listar_companhias.html", context)


@login_required
def adicionar_companhia(request):
    if request.method == "POST":
        adicionar_companhia_form = FormCompanhia(request.POST)

        if adicionar_companhia_form.is_valid():
            adicionar_companhia_form.save()
            return redirect("guarnicao:listar_companhias")

    context = {
        "adicionar_companhia_form": FormCompanhia()}

    return render(request, "gestao/adicionar_companhia.html", context)


@login_required
def remover_companhia(request, id):
    companhia = get_object_or_404(Companhia, id=id)
    if request.method == "POST":
        companhia.delete()

        return redirect("guarnicao:listar_companhias")

    context = {"companhia": companhia}

    return render(request, "gestao/remover_companhia.html", context)


@login_required
def ajax_verifica_guarnicao_ativa(request):
    if request.is_ajax:
        if verifica_guarnicao_ativa(request.user.policial.id):
            return JsonResponse({"ativa": True}, status=200)
    
    return JsonResponse({}, status=200)


def verifica_guarnicao_ativa(id_policial):
    try:
        if Guarnicao.objects.filter(
                comandante_id=id_policial,
                datafechamento=None).last():
            return True
    except Exception:
        return False


def get_guarnicao(id_policial):
    try:
        return Guarnicao.objects.filter(
            comandante_id=id_policial,
            datafechamento=None).last()
    except Exception:
        pass


def get_guarnicoes():
    guarnicoes = Guarnicao.objects.all().order_by("-id")
    return guarnicoes


def get_companhias():
    companhias = Companhia.objects.all().order_by("-id")
    return companhias
