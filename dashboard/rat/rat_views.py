
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import (
    JsonResponse,
    FileResponse
)
from dashboard.guarnicao.guarnicao_views import (
    verifica_guarnicao_ativa,
    get_guarnicao
)
from dashboard.pessoa.forms import FormPessoa
from dashboard.localrecebedor.forms import (
    FormEnvolvidoAgenteRecebedor,
    FormAcessorioAgenteRecebedor
)
from dashboard.observacao.forms import FormObservacao
from dashboard.envolvido.forms import FormEnvolvidoRAT
from dashboard.endereco.forms import FormEndereco
from dashboard.veiculo.forms import FormVeiculo
from dashboard.guarnicao.guarnicao_views import listar_policiais_na_viatura
from .forms import (
    FormRAT,
    FormRATObjetos,
    FormEditarRATObjetos,
    FormRATVeiculos,
    FormEditarRATVeiculos,
    FormRATVeiculoEnvolvidos
)
from django.shortcuts import (
    render,
    redirect
)
from rat.serializers import (
    RATObjetosSerializer,
    ListRATObjetosSerializer,
    RATVeiculosSerializer,
    ListRATVeiculosSerializer,
    ListRATVeiculoEnvolvidosSerializer
)
from rat.models import (
    RAT,
    RATObjetos,
    RATVeiculoEnvolvidos,
    RATVeiculos,
    TipoAcidente
)
from policial.models import Policial
from endereco.models import Municipios
from veiculo.models import Veiculo
from envolvido.models import Envolvido
from django.core.paginator import Paginator
from utils.gerar_pdf import GerarPDF
from django.http import QueryDict
from django.utils import timezone
from anexo.models import Anexo
from anexo.serializers import (
    AnexoSerializer,
    ListAnexoSerializer
)
from dashboard.anexo.forms import FormAnexoRAT
from dashboard.rat.forms import (
    FormEditarRAT,
    FormEditarRelatorio
)
from policialviatura.models import PolicialViatura
from ocorrencia.models import ObservacaoOcorrencia
from ropd.settings import PDF_ROOT


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = RAT.objects.all()
    
    id_exato = request.GET.get("id_exato", "")
    tipoacidente = request.GET.get("tipoacidente", "")
    municipio = request.GET.get("municipio", "")
    placa = request.GET.get("placa", "")
    data_inicial = request.GET.get("data_inicial", "")
    data_final = request.GET.get("data_final", "")

    envolvidos = request.GET.get("envolvidos", "")
    envolvido = request.GET.get("envolvido", "")

    if is_valid_queryparam(id_exato):
        qs = qs.filter(id=id_exato)

    if is_valid_queryparam(tipoacidente):
        qs = qs.filter(tipoacidente=tipoacidente)

    if is_valid_queryparam(municipio):
        qs = qs.filter(endereco__municipio=municipio)
    
    if is_valid_queryparam(placa):
        qs = qs.filter(ratveiculos__veiculo__placa=placa)

    if envolvidos == "on":
        qs = qs.filter(envolvido__isnull=False).distinct()
        if is_valid_queryparam(envolvido):
            qs = qs.filter(envolvido__pessoa__nome__icontains=envolvido)

    if is_valid_queryparam(data_inicial):
        dinicial = timezone.now().strptime(data_inicial, "%d/%m/%Y")
        qs = qs.filter(dataocorrencia__date__gte=dinicial)

    if is_valid_queryparam(data_final):
        dfinal = timezone.now().strptime(data_final, "%d/%m/%Y")
        qs = qs.filter(dataocorrencia__date__lte=dfinal)

    return qs


@login_required
def listar(request):
    qs = filter(request)

    id_tipoacidentes = []
    id_municipios = []

    for rat in RAT.objects.filter(tipoacidente__isnull=False):
        id_tipoacidentes.append(rat.tipoacidente.id)
    
    for rat in RAT.objects.filter(endereco__municipio__isnull=False):
        id_municipios.append(rat.endereco.municipio.codigo_ibge)

    numero_pagina = request.GET.get("pagina", "")

    paginador = Paginator(qs.order_by("-id"), 4)

    filtros = QueryDict(mutable=True)
    checkbox = []

    for k, v in request.GET.items():
        if v != "":
            if k == "id_exato":
                filtros.appendlist("Número", v)
            elif k == "tipoacidente":
                filtros.appendlist("Tipo de acidente", TipoAcidente.objects.get(id=v))
            elif k == "municipio":
                filtros.appendlist("Município", Municipios.objects.get(codigo_ibge=v))
            elif k == "placa":
                filtros.appendlist("Placa", v)
            elif k == "envolvidos":
                checkbox.append("Envolvidos")
            elif k == "envolvido":
                filtros.appendlist("Envolvido", v)
            elif k == "data_inicial":
                filtros.appendlist("Data inicial", v)
            elif k == "data_final":
                filtros.appendlist("Data final", v)

    context = {
        "rats": paginador.get_page(numero_pagina),
        "filtros": filtros,
        "tipoacidentes": TipoAcidente.objects.filter(id__in=id_tipoacidentes).distinct(),
        "municipios": Municipios.objects.filter(codigo_ibge__in=id_municipios).distinct(),
        "checkbox": checkbox
    }

    return render(request, "rat/listar.html", context)


@login_required
def mostrar(request, id):
    rat = RAT.objects.get(id=id)

    context = {
        "rat": rat,
        "pms": listar_policiais_na_viatura(rat.guarnicao_id),
    }

    return render(request, "rat/mostrar.html", context)


from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def geraemostrapdfrat(request, id):
    try:
        rat = RAT.objects.get(id=id)

        pasta = "rats/"
        nomearquivo = "RAT_" + str(rat.id) + "-" +\
            timezone.localtime(rat.dataocorrencia).strftime("%Y")
        arquivo = pasta + str(nomearquivo + ".pdf").replace(" ", "_")
        
        filename = PDF_ROOT + pasta + str(nomearquivo + ".pdf").replace(" ", "_")

        context_pdf = {
            "rat": rat,
            "pms": PolicialViatura.objects.filter(
                guarnicao=rat.guarnicao).order_by(
                    "policial__nomeguerra"),
            "envolvidos": Envolvido.objects.filter(
                rat=rat),
            "objetos": RATObjetos.objects.filter(rat=rat),
            "veiculos": RATVeiculos.objects.filter(rat=rat),
            "anexos": Anexo.objects.filter(rat=rat)
        }

        GerarPDF("rat/pdf.html", context_pdf, arquivo)

        with open(filename, 'r'):
            response = FileResponse(open(filename))
            return response

    except Exception as error:
        raise error


@login_required
def edit_rat(request, id):
    try:
        rat = RAT.objects.get(id=id)

        context = {
            "id": rat.id,
            "rat": FormEditarRAT(instance=rat)
        }

        return render(request, "rat/edits/edit_rat.html", context)
    except Exception:
        pass


@login_required
def post_edit_rat(request):
    if request.is_ajax and request.method == "POST":
        instance = RAT.objects.get(
            id=request.POST.get("id_rat"))

        rat = FormEditarRAT(request.POST, instance=instance)

        if rat.is_valid():
            rat.save()

            return JsonResponse({"message": "RAT atualizada."}, status=200)
        else:
            return JsonResponse(rat.errors, status=400)


@login_required
def edit_relatorio(request, id):
    try:
        rat = RAT.objects.get(id=id)

        context = {
            "id": rat.id,
            "rat": FormEditarRelatorio(instance=rat)
        }

        return render(request, "rat/edits/edit_relatorio.html", context)
    except Exception:
        pass


@login_required
def post_edit_relatorio(request):
    if request.is_ajax and request.method == "POST":
        instance = RAT.objects.get(id=request.POST.get("id_rat"))

        relatorio = FormEditarRelatorio(request.POST, instance=instance)

        if relatorio.is_valid():
            relatorio.save()

            return JsonResponse(
                {"message": "Relatório atualizado."}, status=200)
        else:
            return JsonResponse(relatorio.errors, status=400)


def verifica_rat_nao_finalizada(request):
    if request.is_ajax:
        pendentes = RAT.objects.filter(
            guarnicao__comandante=request.user.policial.id,
            relatorio__isnull=True)

        return JsonResponse({"pendentes": pendentes.count()}, status=200)
        
    return JsonResponse({}, status=200)


@login_required
def listar_rats_sem_finalizar(request):
    rats = RAT.objects.filter(
        guarnicao__comandante=request.user.policial.id,
        relatorio__isnull=True)

    context = {"rats": rats}

    return render(request, "rat/sem_finalizar.html", context)


@login_required
@csrf_exempt
def checa_policial_guarnicao(request):
    if request.is_ajax and request.method == "POST":
        policial = request.user.policial.id
        if verifica_guarnicao_ativa(policial):
            return JsonResponse({
                "redirect": reverse("rat:adicionar_rat")
            }, status=200)
        else:
            return JsonResponse({
                "error": "Você não possui uma guarnição"
                         " ativa para adicionar um RAT!"
            }, status=400)

    return JsonResponse({}, status=400)


@login_required
def adicionar_rat(request):
    policial = request.user.policial.id
    guarnicao = get_guarnicao(policial)
    if verifica_guarnicao_ativa(policial) and guarnicao.ativo:
        context = {
            "guarnicao": guarnicao,
            "rat": FormRAT(),
            "endereco": FormEndereco(),
            "observacao": FormObservacao(),
        }

        return render(request, "rat/adicionar_rat.html", context)
    else:
        return redirect("index")


@login_required
def post_rat(request):
    if request.is_ajax and request.method == "POST":
        rat = FormRAT(request.POST or None)
        endereco = FormEndereco(request.POST or None)
        observacao = FormObservacao(request.POST or None)

        if rat.is_valid()\
                and endereco.is_valid():

            endereco = endereco.save(commit=False)

            if observacao.is_valid():
                endereco.observacao = observacao.save()
                endereco.save()
            else:
                endereco.save()

            rat = rat.save(commit=False)
            rat.endereco = endereco
            rat.save()

            return JsonResponse({
                "redirect": reverse(
                    "rat:adicionar_veiculos_envolvidos",
                    kwargs={"rat": rat.id})
            }, status=200)
        else:
            return JsonResponse({
                "rat": rat.errors,
                "endereco": endereco.errors
            }, status=400)

    return JsonResponse({"error": ""}, status=400)


@login_required
def adicionar_veiculos_envolvidos(request, rat):
    try:
        rat = RAT.objects.get(id=rat)
        if rat.relatorio is None:

            context = {
                "rat": rat,
                "ratobjeto": FormRATObjetos(),
                "ratenvolvido": FormEnvolvidoRAT(),
                "veiculo": FormVeiculo(),
                "ratveiculo": FormRATVeiculos(),
                "pessoa": FormPessoa(),
                "ratveiculoenvolvidos": FormRATVeiculoEnvolvidos(),
                "ratagenterecebedor_envolvido": FormEnvolvidoAgenteRecebedor(),
                "agenterecebedor": FormAcessorioAgenteRecebedor(),
                "observacao": FormObservacao(),
                "versao": FormObservacao(),
                "anexo": FormAnexoRAT()
            }

            return render(
                request,
                "rat/adicionar_veiculos_envolvidos.html",
                context)
        else:
            return redirect("index")
    except Exception:
        pass


# ANEXOS
@login_required
def get_anexos(request):
    try:
        rat = request.GET.get("rat")
        anexos = Anexo.objects.filter(rat=rat).order_by("id")
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
        anexo = FormAnexoRAT(request.POST, request.FILES or None)
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


# OBJETOS
@login_required
def get_objetos(request):
    try:
        rat = request.GET.get("rat", None)
        objetos = RATObjetos.objects.filter(rat=rat).order_by("-id")
    except Exception:
        pass

    data = dict()

    if objetos:
        serializer = ListRATObjetosSerializer(objetos, many=True)
        data["objetos"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_objeto(request):
    if request.is_ajax and request.method == "POST":
        objeto = FormRATObjetos(
            request.POST or None)

        if objeto.is_valid():
            objeto = objeto.save()

            instance = RATObjetosSerializer(objeto).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse(objeto.errors, status=400)

    return JsonResponse({"error": ""}, status=400)


@login_required
def edit_objeto(request, id):
    try:
        objeto = RATObjetos.objects.get(id=id)

        context = {
            "id": objeto.id,
            "objeto": FormEditarRATObjetos(instance=objeto)
        }

        return render(request, "rat/edits/edit_objeto.html", context)
    except Exception:
        pass


@login_required
def post_edit_objeto(request):
    if request.is_ajax and request.method == "POST":
        instance = RATObjetos.objects.get(
            id=request.POST.get("id_objeto"))

        objeto = FormEditarRATObjetos(request.POST, instance=instance)

        if objeto.is_valid():
            objeto.save()

            return JsonResponse({"message": "Objeto atualizado."}, status=200)
        else:
            return JsonResponse(objeto.errors, status=400)


@login_required
@csrf_exempt
def delete_objeto(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            objeto = RATObjetos.objects.get(id=id)

            data = dict()

            if objeto:
                objeto.delete()
                data["message"] = "Objeto removido."

            return JsonResponse(data)
        except Exception as error:
            raise error


# VEÍCULOS
@login_required
def get_veiculos(request):
    try:
        rat = request.GET.get("rat", None)
        veiculos = RATVeiculos.objects.filter(
            rat=rat).order_by("-id")
    except Exception:
        pass

    data = dict()

    if veiculos:
        serializer = ListRATVeiculosSerializer(
            veiculos, many=True)
        data["veiculos"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_veiculo(request):
    if request.is_ajax and request.method == "POST":
        veiculo = FormVeiculo(request.POST or None)
        ratveiculo = FormRATVeiculos(request.POST or None)
        agenterecebedor = FormAcessorioAgenteRecebedor(request.POST or None)
        observacao = FormObservacao(request.POST or None)

        if veiculo.is_valid()\
            and ratveiculo.is_valid()\
                and agenterecebedor.is_valid():

            ratveiculo = ratveiculo.save(commit=False)
            ratveiculo.veiculo = veiculo.save()
            ratveiculo.agenterecebedor = agenterecebedor.save()

            if observacao.is_valid():
                ratveiculo.observacao = observacao.save()

            ratveiculo.save()

            instance = ListRATVeiculosSerializer(ratveiculo).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse({
                "veiculo": veiculo.errors,
                "ratveiculo": ratveiculo.errors
            }, status=400)

    return JsonResponse({"error": ""}, status=400)


@login_required
def checar_veiculo_placa_existente(request):
    if request.is_ajax and request.method == "GET":
        placa = request.GET.get("placa", None)
        rat = request.GET.get("rat")

        if RATVeiculos.objects.filter(
                veiculo__placa=placa,
                rat=rat).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)


@login_required
def checar_veiculo_chassi_existente(request):
    if request.is_ajax and request.method == "GET":
        chassi = request.GET.get("chassi", None)
        rat = request.GET.get("rat")

        if RATVeiculos.objects.filter(
                veiculo__chassi=chassi,
                rat=rat).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)


@login_required
def edit_veiculo(request, id):
    try:
        veiculo = Veiculo.objects.get(id=id)

        context = {
            "id": veiculo.id,
            "veiculo": FormVeiculo(instance=veiculo)
        }

        return render(request, "ocorrencia/edits/edit_veiculo.html", context)
    except Exception:
        pass


@login_required
def post_edit_veiculo(request):
    if request.is_ajax and request.method == "POST":
        veiculo_instance = Veiculo.objects.get(
            id=request.POST.get("id_veiculo"))
        veiculo_ap_instance = Veiculo.objects.get(
            tipo=veiculo_instance)

        veiculo = FormVeiculo(request.POST, instance=veiculo_instance)
        veiculo_ap = FormVeiculo(
            request.POST, instance=veiculo_ap_instance)

        if veiculo.is_valid()\
                and veiculo_ap.is_valid():
            veiculo.save()
            veiculo_ap.save()

            return JsonResponse({"message": "Veículo atualizado."}, status=200)
        else:
            return JsonResponse({
                "veiculo": veiculo.errors,
                "veiculo_ap": veiculo_ap.errors
                }, status=400)


@login_required
@csrf_exempt
def delete_veiculo(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            veiculo = Veiculo.objects.get(id=id)

            data = dict()

            if veiculo:
                veiculo.delete()
                data["message"] = "Veículo removido."

            return JsonResponse(data)
        except Exception as error:
            raise error


@login_required
@csrf_exempt
def post_preview_rat(request):
    if request.is_ajax and request.method == "POST":
        id = request.POST.get("rat")
        relatorio = request.POST.get("relatorio")
        rat = RAT.objects.get(id=id)

        rat.relatorio = relatorio
        rat.save()

        return JsonResponse({
            "redirect": reverse(
                "rat:preview_rat",
                kwargs={"id": id})
            }, status=200)


@login_required
def preview_rat(request, id):
    try:
        rat = get_rat(id)

        context = {
            "rat": rat,
            "pms": listar_policiais_na_viatura(rat.guarnicao_id)
        }

        return render(request, "rat/finalizar_rat.html", context)
    except Exception:
        return redirect("index")


@login_required
@csrf_exempt
def post_delete_rat(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("rat")
            rat = RAT.objects.get(id=id)

            if rat:
                rat.delete()

            return JsonResponse({"redirect": reverse("index")}, status=200)
        except Exception:
            pass


def get_rat(id):
    try:
        rat = RAT.objects.get(id=id)
        return rat
    except Exception:
        pass
