from django.shortcuts import (
    render,
    redirect
)
from pathlib import Path
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from ropd.settings import (
    MEDIA_URL,
    PDF_ROOT
)
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# UTILS
from django.utils import timezone
from utils.gerar_pdf import GerarPDF
from utils.extrair_lat_lng import extract_lat_lng

# HTTP
from django.http import (
    QueryDict,
    JsonResponse,
    FileResponse,
    HttpResponse
)

# VIEWS
from dashboard.policialviatura.policialviatura_views import (
    listar_policiais_na_viatura
)
from dashboard.guarnicao.guarnicao_views import (
    verifica_guarnicao_ativa,
    get_guarnicao
)
from dashboard.envolvido.envolvido_views import (
    post_envolvidoocorrencia
)
from dashboard.acessoriosocorrencia.acessorios_views import (
    post_arma,
    post_droga,
    post_diverso,
    post_doc,
    post_municao,
    post_veiculo
)

# MODELS
from ocorrencia.models import (
    Ocorrencia,
    Infracao,
    ObservacaoOcorrencia
)
from policial.models import Policial
from policialviatura.models import PolicialViatura
from envolvido.models import Envolvido
from acessoriosocorrencia.models import (
    AcessoriosOcorrencia,
    ArmaAcessorio,
    DiversosAcessorio,
    DocAcessorio,
    DrogaAcessorio,
    MunicaoAcessorio,
    VeiculoAcessorio
)
from pessoa.models import Pessoa
from guarnicao.models import Guarnicao

# SERIALIZERS
from ocorrencia.serializers import (
    ListObservacaoOcorrenciaSerializer,
    ObservacaoOcorrenciaSerializer
)

# FORMS
from .forms import (
    FormOcorrencia,
    FormEditarRelatorio,
    FormObservacaoOcorrencia
)
from dashboard.endereco.forms import FormEndereco
from dashboard.envolvido.forms import FormEnvolvido
from dashboard.veiculo.forms import FormVeiculo
from dashboard.acessoriosocorrencia.forms import (
    FormArma,
    FormArmaAcessorio,
    FormDrogaAcessorio,
    FormDiversosAcessorio,
    FormDocAcessorio,
    FormMunicaoAcessorio,
    FormVeiculoAcessorio
)
from dashboard.localrecebedor.forms import (
    FormEnvolvidoAgenteRecebedor,
    FormAcessorioAgenteRecebedor
)
from dashboard.pessoa.forms import FormPessoa
from dashboard.observacao.forms import FormObservacao

# PDF
import io
from reportlab.pdfgen import canvas


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Ocorrencia.objects.all()
    
    id_exato = request.GET.get("id_exato", "")
    infracao = request.GET.get("infracao", "")
    policial = request.GET.get("policial", "")
    data_inicial = request.GET.get("data_inicial", "")
    data_final = request.GET.get("data_final", "")

    envolvidos = request.GET.get("envolvidos", "")
    envolvido = request.GET.get("envolvido", "")

    armas = request.GET.get("armas", "")
    diversos = request.GET.get("diversos", "")
    docs = request.GET.get("docs", "")
    drogas = request.GET.get("drogas", "")
    municoes = request.GET.get("municoes", "")
    veiculos = request.GET.get("veiculos", "")

    if is_valid_queryparam(id_exato):
        qs = qs.filter(id=id_exato)

    if is_valid_queryparam(infracao):
        qs = qs.filter(infracao=infracao)

    if is_valid_queryparam(policial):
        qs = qs.filter(guarnicao__comandante=policial)

    if is_valid_queryparam(data_inicial):
        dinicial = timezone.now().strptime(data_inicial, "%d/%m/%Y")
        qs = qs.filter(dataocorrencia__date__gte=dinicial)

    if is_valid_queryparam(data_final):
        dfinal = timezone.now().strptime(data_final, "%d/%m/%Y")
        qs = qs.filter(dataocorrencia__date__lte=dfinal)

    if envolvidos == "on":
        qs = qs.filter(envolvido__isnull=False).distinct()
        if is_valid_queryparam(envolvido):
            qs = qs.filter(envolvido__pessoa__nome__icontains=envolvido)

    if armas == "on":
        qs = qs.filter(
            acessoriosocorrencia__armaacessorio__isnull=False).distinct()

    if diversos == "on":
        qs = qs.filter(
            acessoriosocorrencia__diversosacessorio__isnull=False).distinct()

    if docs == "on":
        qs = qs.filter(
            acessoriosocorrencia__docacessorio__isnull=False).distinct()

    if drogas == "on":
        qs = qs.filter(
            acessoriosocorrencia__drogaacessorio__isnull=False).distinct()

    if municoes == "on":
        qs = qs.filter(
            acessoriosocorrencia__municaoacessorio__isnull=False).distinct()

    if veiculos == "on":
        qs = qs.filter(
            acessoriosocorrencia__veiculoacessorio__isnull=False).distinct()

    return qs


@login_required
def listar(request):
    qs = filter(request)

    numero_pagina = request.GET.get("pagina", "")

    paginador = Paginator(qs.order_by("-id"), 4)

    id_policiais = []
    id_infracoes = []

    for guarnicao in Guarnicao.objects.filter(ocorrencia__isnull=False):
        id_policiais.append(guarnicao.comandante.id)

    for ocorrencia in Ocorrencia.objects.filter(infracao__isnull=False):
        id_infracoes.append(ocorrencia.infracao.id)

    filtros = QueryDict(mutable=True)
    checkbox = []

    for k, v in request.GET.items():
        if v != "":
            if k == "id_exato":
                filtros.appendlist("Número", v)
            elif k == "infracao":
                filtros.appendlist("Infração", Infracao.objects.get(id=v))
            elif k == "policial":
                filtros.appendlist(
                    "Comandante da Guarnição", Policial.objects.get(id=v))
            elif k == "data_inicial":
                filtros.appendlist("Data inicial", v)
            elif k == "data_final":
                filtros.appendlist("Data final", v)
            elif k == "envolvidos":
                checkbox.append("Envolvidos")
            elif k == "envolvido":
                filtros.appendlist("Envolvido", v)
            elif k == "armas":
                checkbox.append("Armas")
            elif k == "diversos":
                checkbox.append("Objetos")
            elif k == "docs":
                checkbox.append("Documentos")
            elif k == "drogas":
                checkbox.append("Drogas")
            elif k == "municoes":
                checkbox.append("Munições")
            elif k == "veiculos":
                checkbox.append("Veículos")

    context = {
        "ocorrencias": paginador.get_page(numero_pagina),
        "policiais": Policial.objects.filter(id__in=id_policiais).distinct(),
        "infracoes": Infracao.objects.filter(id__in=id_infracoes).distinct(),
        "filtros": filtros,
        "checkbox": checkbox
    }

    return render(request, "ocorrencia/listar.html", context)


@login_required
def mostrar(request, id):
    ocorrencia = Ocorrencia.objects.get(id=id)

    context = {
        "ocorrencia": ocorrencia,
        "pms": listar_policiais_na_viatura(
                   get_ocorrencia(id).guarnicao_id),
        "observacao": FormObservacao(),
        "observacaoocorrencia": FormObservacaoOcorrencia()
    }

    return render(request, "ocorrencia/mostrar.html", context)

from django.views.decorators.clickjacking import xframe_options_exempt

from utils.pycrypto import encrypt, decrypt


@xframe_options_exempt
def geraemostrapdfocorrencia(request, id):
    try:
        ocorrencia = Ocorrencia.objects.get(id=id)

        pasta = "ocorrencias/"
        nomearquivo = "Ocorrencia_" + str(ocorrencia.id) + "-" +\
            timezone.localtime(ocorrencia.dataocorrencia).strftime("%Y")
        arquivo = pasta + str(nomearquivo + ".pdf").replace(" ", "_")
        
        filename = PDF_ROOT + pasta + str(nomearquivo + ".pdf").replace(" ", "_")
    
        message = """ID DA GUARNIÇÃO: {}
MATRÍCULA DO COMANDANTE DA GUARNIÇÃO: {}
ID DA OCORRÊNCIA: {}
DATA CRIAÇÃO DA OCORRÊNCIA: {}""".format(
            ocorrencia.guarnicao.id,
            ocorrencia.guarnicao.comandante.id,
            ocorrencia.id,
            ocorrencia.datacriacao)

        context_pdf = {
            "ocorrencia": ocorrencia,
            "pms": PolicialViatura.objects.filter(
                guarnicao=ocorrencia.guarnicao).order_by(
                    "policial__nomeguerra"),
            "envolvidos": Envolvido.objects.filter(
                ocorrencia=ocorrencia),
            "anexos": Anexo.objects.filter(ocorrencia=ocorrencia),
            "aditamentos": ObservacaoOcorrencia.objects.filter(ocorrencia=ocorrencia),
            "hash": encrypt("3ut3nh04f0rc@2021", message)
        }

        try:
            acessoriosocorrencia = AcessoriosOcorrencia.objects.get(ocorrencia=ocorrencia)
            aoid = acessoriosocorrencia.id

            context_pdf["armas"] = ArmaAcessorio.objects.filter(
                acessoriosocorrencia=aoid)
            context_pdf["drogas"] = DrogaAcessorio.objects.filter(
                acessoriosocorrencia=aoid)
            context_pdf["diversos"] = DiversosAcessorio.objects.filter(
                acessoriosocorrencia=aoid)
            context_pdf["docs"] = DocAcessorio.objects.filter(
                acessoriosocorrencia=aoid)
            context_pdf["municoes"] =  MunicaoAcessorio.objects.filter(
                acessoriosocorrencia=aoid)
            context_pdf["veiculos"] = VeiculoAcessorio.objects.filter(
                acessoriosocorrencia=aoid)
        except Exception:
            pass

        GerarPDF("ocorrencia/pdf.html", context_pdf, arquivo)

        with open(filename, 'r'):
            response = FileResponse(open(filename))
            return response

    except Exception as error:
        raise error


@login_required
def verifica_ocorrencia_nao_finalizada(request):
    if request.is_ajax:
        pendentes = Ocorrencia.objects.filter(
            guarnicao__comandante=request.user.policial.id,
            relatorio__isnull=True)

        return JsonResponse({"pendentes": pendentes.count()}, status=200)
        
    return JsonResponse({}, status=200)


@login_required
def listar_ocorrencias_sem_finalizar(request):
    ocorrencias = Ocorrencia.objects.filter(
        guarnicao__comandante=request.user.policial.id,
        relatorio__isnull=True)

    context = {"ocorrencias": ocorrencias}

    return render(request, "ocorrencia/sem_finalizar.html", context)


# ADICIONAR OCORRÊNCIA
@login_required
@csrf_exempt
def checa_policial_guarnicao(request):
    if request.is_ajax and request.method == "POST":
        policial = request.user.policial.id
        if verifica_guarnicao_ativa(policial):
            return JsonResponse({
                "redirect": reverse("ocorrencia:adicionar_ocorrencia")
            }, status=200)
        else:
            return JsonResponse({
                "error": "Você não possui uma guarnição"
                         " ativa para adicionar ocorrência!"
            }, status=400)

    return JsonResponse({}, status=400)


@login_required
def adicionar_ocorrencia(request):
    policial = request.user.policial.id
    guarnicao = get_guarnicao(policial)
    if verifica_guarnicao_ativa(policial) and guarnicao.ativo:
        context = {
            "guarnicao": guarnicao,
            "ocorrencia": FormOcorrencia(),
            "endereco": FormEndereco(),
            "observacao": FormObservacao(),
        }

        return render(request, "ocorrencia/adicionar_ocorrencia.html", context)
    else:
        return redirect("index")


@login_required
def post_ocorrencia(request):
    if request.is_ajax and request.method == "POST":
        ocorrencia = FormOcorrencia(request.POST or None)
        endereco = FormEndereco(request.POST or None)
        observacao = FormObservacao(request.POST or None)

        if ocorrencia.is_valid()\
                and endereco.is_valid():

            endereco = endereco.save(commit=False)

            if endereco.numero is None:
                numero = ""
            else:
                numero = ", " + endereco.numero

            address = "{}, {}, Rua {}{}".format(
                endereco.municipio, endereco.bairro, endereco.rua, numero)

            geolocalizacao = extract_lat_lng(address)

            endereco.latitude = geolocalizacao[0]
            endereco.longitude = geolocalizacao[1]

            if observacao.is_valid():
                endereco.observacao = observacao.save()
                endereco.save()
            else:
                endereco.save()

            ocorrencia = ocorrencia.save(commit=False)
            ocorrencia.endereco = endereco
            ocorrencia.save()

            AcessoriosOcorrencia.objects.create(
                ocorrencia_id=ocorrencia.id)

            return JsonResponse({
                "redirect": reverse(
                    "ocorrencia:adicionar_acessorios",
                    kwargs={"ocorrencia": ocorrencia.id})
            }, status=200)
        else:
            return JsonResponse({
                "ocorrencia": ocorrencia.errors,
                "endereco": endereco.errors
            }, status=400)

    return JsonResponse({"error": ""}, status=400)

from dashboard.anexo.forms import FormAnexoOcorrencia
from anexo.models import Anexo
from anexo.serializers import ListAnexoSerializer

@login_required
def adicionar_acessorios(request, ocorrencia):
    try:
        if Ocorrencia.objects.get(id=ocorrencia).relatorio is None:
            acessoriosocorrencia = AcessoriosOcorrencia.objects.get(
                ocorrencia_id=ocorrencia).id

            context = {
                "objeto_ocorrencia": Ocorrencia.objects.get(id=ocorrencia),
                "ocorrencia": ocorrencia,
                "acessoriosocorrencia": acessoriosocorrencia,
                "pessoa": FormPessoa(),
                "envolvido": FormEnvolvido(),
                "arma": FormArma(),
                "armaacessorio": FormArmaAcessorio(),
                "drogaacessorio": FormDrogaAcessorio(),
                "diversosacessorio": FormDiversosAcessorio(),
                "docacessorio": FormDocAcessorio(),
                "municaoacessorio": FormMunicaoAcessorio(),
                "veiculo": FormVeiculo(),
                "veiculoacessorio": FormVeiculoAcessorio(),
                "agenterecebedor_envolvido": FormEnvolvidoAgenteRecebedor(),
                "agenterecebedor": FormAcessorioAgenteRecebedor(),
                "observacao": FormObservacao(),
                "anexo": FormAnexoOcorrencia()
            }
            return render(
                request,
                "ocorrencia/adicionar_acessorios.html",
                context)
        else:
            return redirect("index")
    except Exception:
        pass


# ANEXOS
@login_required
def get_anexos(request):
    try:
        ocorrencia = request.GET.get("ocorrencia")
        anexos = Anexo.objects.filter(ocorrencia=ocorrencia).order_by("id")
    except Exception:
        pass

    data = dict()

    if anexos:
        serializer = ListAnexoSerializer(anexos, many=True)
        data["anexos"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_anexo(request):
    if request.is_ajax and request.method == "POST":
        anexo = FormAnexoOcorrencia(request.POST, request.FILES or None)
        observacao = FormObservacao(request.POST or None)

        if anexo.is_valid():
            anexo = anexo.save(commit=False)
            anexo.observacao = observacao.save()
            anexo.save()

            return JsonResponse({}, status=200)
        else:
            return JsonResponse(anexo.errors, status=400)

    return JsonResponse({}, status=400)


@login_required
@csrf_exempt
def delete_anexo(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            anexo = Anexo.objects.get(id=id)

            data = dict()

            if anexo:
                anexo.delete()
                data["message"] = "Anexo removido."

            return JsonResponse(data)
        except Exception as error:
            raise error


@login_required
def vincular_ocorrencia(request, id):
    try:
        paginador = Paginator(Ocorrencia.objects.all(), 3)
        numero_pagina = request.GET.get("pagina")

        context = {
            "ocorrencia": Ocorrencia.objects.get(id=id),
            "ocorrencias": paginador.get_page(numero_pagina),
        }

        return render(request, "ocorrencia/includes/vincular_ocorrencia.html", context)
    except Exception:
        pass


@login_required
@csrf_exempt
def post_vincular_ocorrencia(request):
    if request.is_ajax and request.method == "POST":
        ocorrencia = Ocorrencia.objects.get(id=request.POST.get("ocorrencia", ""))
        vinculo = Ocorrencia.objects.get(id=request.POST.get("vinculo", ""))

        ocorrencia.vinculo = vinculo
        ocorrencia.save()

        return JsonResponse({"message": "Ocorrência vinculada com sucesso!"}, status=200)
    else:
        return JsonResponse({}, status=200)


@login_required
@csrf_exempt
def post_preview_ocorrencia(request):
    if request.is_ajax and request.method == "POST":
        id = request.POST.get("ocorrencia")
        relatorio = request.POST.get("relatorio")
        ocorrencia = Ocorrencia.objects.get(id=id)

        ocorrencia.relatorio = relatorio
        ocorrencia.save()

        return JsonResponse({
            "redirect": reverse(
                "ocorrencia:preview_ocorrencia",
                kwargs={"id": id})
            }, status=200)


@login_required
def preview_ocorrencia(request, id):
    ocorrencia = get_ocorrencia(id)
    if ocorrencia.guarnicao.comandante == request.user.policial and ocorrencia.status_previa:
        try:
            context = {
                "ocorrencia": ocorrencia,
                "pms": listar_policiais_na_viatura(ocorrencia.guarnicao_id)
            }

            return render(request, "ocorrencia/finalizar_ocorrencia.html", context)
        except Exception:
            return redirect("index")
    else:
        return redirect("index")


@login_required
def edit_relatorio(request, id):
    try:
        ocorrencia = Ocorrencia.objects.get(id=id)

        context = {
            "id": ocorrencia.id,
            "ocorrencia": FormEditarRelatorio(instance=ocorrencia)
        }

        return render(request, "ocorrencia/edits/edit_relatorio.html", context)
    except Exception:
        pass


@login_required
def post_edit_relatorio(request):
    if request.is_ajax and request.method == "POST":
        instance = Ocorrencia.objects.get(id=request.POST.get("id_ocorrencia"))

        relatorio = FormEditarRelatorio(request.POST, instance=instance)

        if relatorio.is_valid():
            relatorio.save()

            return JsonResponse(
                {"message": "Relatório atualizado."}, status=200)
        else:
            return JsonResponse(relatorio.errors, status=400)


@login_required
def get_aditamentos(request):
    try:
        ocorrencia = request.GET.get("ocorrencia", None)
        aditamentos = ObservacaoOcorrencia.objects.filter(
            ocorrencia=ocorrencia).order_by("id")
    except Exception:
        pass

    data = dict()

    if aditamentos:
        serializer = ListObservacaoOcorrenciaSerializer(aditamentos, many=True)
        data["aditamentos"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_aditamento(request):
    if request.is_ajax and request.method == "POST":
        observacao = FormObservacao(request.POST or None)
        observacaoocorrencia = FormObservacaoOcorrencia(request.POST or None)

        if observacao.is_valid()\
                and observacaoocorrencia.is_valid():
            observacaoocorrencia = observacaoocorrencia.save(commit=False)
            observacaoocorrencia.observacao = observacao.save()
            observacaoocorrencia.autor = Policial.objects.get(id=request.user.policial.id)
            observacaoocorrencia.save()

            return JsonResponse({}, status=200)
        else:
            return JsonResponse(observacaoocorrencia.errors, status=400)


@login_required
@csrf_exempt
def cancel_aditamento(request):
    if request.is_ajax and request.method == "POST":
        try:
            observacao = ObservacaoOcorrencia.objects.get(id=request.POST.get("id"))

            data = dict()

            if observacao:
                observacao.ativo = False
                observacao.save()
                data["message"] = "Observação cancelada."

            return JsonResponse(data)
        except Exception as error:
            raise error


@login_required
def get_apreensoes(request):
    if request.is_ajax and request.method == "GET":
        ocorrencia = request.GET.get("ocorrencia", "")

        data = dict()

        envolvidos = Envolvido.objects.filter(
            ocorrencia=ocorrencia).order_by("-id")
        if envolvidos:
            data["envolvidos"] = True

        try:
            acessoriosocorrencia = AcessoriosOcorrencia.objects.get(
                ocorrencia_id=ocorrencia).id
            data["acessoriosocorrencia"] = acessoriosocorrencia

            armas = ArmaAcessorio.objects.filter(
                    acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
            if armas:
                data["armas"] = True

            drogas = DrogaAcessorio.objects.filter(
                acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
            if drogas:
                data["drogas"] = True

            diversos = DiversosAcessorio.objects.filter(
                acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
            if diversos:
                data["diversos"] = True

            docs = DocAcessorio.objects.filter(
                acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
            if docs:
                data["docs"] = True

            municoes = MunicaoAcessorio.objects.filter(
                acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
            if municoes:
                data["municoes"] = True

            veiculos = VeiculoAcessorio.objects.filter(
                acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
            if veiculos:
                data["veiculos"] = True

        except Exception:
            pass

        return JsonResponse(data, status=200)


@login_required
@csrf_exempt
def post_delete_ocorrencia(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("ocorrencia")
            ocorrencia = Ocorrencia.objects.get(id=id)

            if ocorrencia:
                ocorrencia.delete()

            return JsonResponse({"redirect": reverse("index")}, status=200)
        except Exception:
            pass


@login_required
@csrf_exempt
def finalizar_ocorrencia(request):
    if request.is_ajax and request.method == "POST":
        ocorrencia = Ocorrencia.objects.get(id=request.POST.get("ocorrencia"))

        ocorrencia.status_previa = False
        ocorrencia.save()

        acessoriosocorrencia = AcessoriosOcorrencia.objects.get(
                           ocorrencia=ocorrencia)
        aoid = acessoriosocorrencia.id

        if not (ArmaAcessorio.objects.filter(
                acessoriosocorrencia=aoid).exists()
                or DrogaAcessorio.objects.filter(
                    acessoriosocorrencia=aoid).exists()
                or DiversosAcessorio.objects.filter(
                    acessoriosocorrencia=aoid).exists()
                or DocAcessorio.objects.filter(
                    acessoriosocorrencia=aoid).exists()
                or MunicaoAcessorio.objects.filter(
                    acessoriosocorrencia=aoid).exists()
                or VeiculoAcessorio.objects.filter(
                    acessoriosocorrencia=aoid).exists()):
            acessoriosocorrencia.delete()

        return JsonResponse({
            "redirect": reverse("ocorrencia:listar")
        }, status=200)
# ACABA AQUI


def get_ocorrencias(comandante):
    ocorrencias = Ocorrencia.objects.filter(
        guarnicao=get_guarnicao(comandante))
    return ocorrencias


def get_ocorrencia(id):
    try:
        ocorrencia = Ocorrencia.objects.get(id=id)
        return ocorrencia
    except Exception:
        pass
