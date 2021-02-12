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
import io

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
from guarnicao.models import (
    Guarnicao,
    Companhia
)
from endereco.models import Municipios

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
from reportlab.pdfgen import canvas

# EXCEL
import xlwt

from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Count, Max, Min
import itertools


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Ocorrencia.objects.all()
    
    id_exato = request.GET.get("id_exato", "")
    infracao = request.GET.get("infracao", "")
    cidade = request.GET.get("cidade", "")
    companhia = request.GET.get("companhia", "")
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
    
    if is_valid_queryparam(cidade):
        qs = qs.filter(endereco__municipio__codigo_ibge=cidade)

    if is_valid_queryparam(companhia):
        qs = qs.filter(guarnicao__companhia=companhia)

    if is_valid_queryparam(data_inicial):
        dinicial = timezone.now().strptime(data_inicial, "%d/%m/%Y")
        qs = qs.filter(dataocorrencia__date__gte=dinicial)

    if is_valid_queryparam(data_final):
        dfinal = timezone.now().strptime(data_final, "%d/%m/%Y")
        qs = qs.filter(dataocorrencia__date__lte=dfinal)

    if envolvidos == "on":
        qs = qs.filter(envolvido_ocorrencia__isnull=False).distinct()
        if is_valid_queryparam(envolvido):
            qs = qs.filter(envolvido_ocorrencia__pessoa__nome__icontains=envolvido)

    if armas == "on":
        qs = qs.filter(
            acessoriosocorrencia_ocorrencia__armaacessorio_acessoriosocorrencia__isnull=False).distinct()

    if diversos == "on":
        qs = qs.filter(
            acessoriosocorrencia_ocorrencia__diversosacessorio_acessoriosocorrencia__isnull=False).distinct()

    if docs == "on":
        qs = qs.filter(
            acessoriosocorrencia_ocorrencia__docacessorio_acessoriosocorrencia__isnull=False).distinct()

    if drogas == "on":
        qs = qs.filter(
            acessoriosocorrencia_ocorrencia__drogaacessorio_acessoriosocorrencia__isnull=False).distinct()

    if municoes == "on":
        qs = qs.filter(
            acessoriosocorrencia_ocorrencia__municaoacessorio_acessoriosocorrencia__isnull=False).distinct()

    if veiculos == "on":
        qs = qs.filter(
            acessoriosocorrencia_ocorrencia__veiculoacessorio_acessoriosocorrencia__isnull=False).distinct()

    return qs


@login_required
def listar(request):
    qs = filter(request)

    numero_pagina = request.GET.get("pagina", "")

    paginador = Paginator(qs.order_by("-id"), 4)

    id_cidades = []
    id_companhias = []
    id_infracoes = []

    for ocorrencia in Ocorrencia.objects.filter(infracao__isnull=False):
        id_cidades.append(ocorrencia.endereco.municipio.codigo_ibge)
        id_companhias.append(ocorrencia.guarnicao.companhia.id)
        id_infracoes.append(ocorrencia.infracao.id)

    filtros = QueryDict(mutable=True)
    checkbox = []

    for k, v in request.GET.items():
        if v != "":
            if k == "id_exato":
                filtros.appendlist("Número", v)
            elif k == "infracao":
                filtros.appendlist("Infração", Infracao.objects.get(id=v))
            elif k == "cidade":
                filtros.appendlist("Cidade", Municipios.objects.get(codigo_ibge=v))
            elif k == "companhia":
                filtros.appendlist("Companhia", Companhia.objects.get(id=v))
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
        "cidades": Municipios.objects.filter(codigo_ibge__in=id_cidades).distinct().order_by("nome"),
        "companhias": Companhia.objects.filter(id__in=id_companhias).distinct().order_by("companhia"),
        "infracoes": Infracao.objects.filter(id__in=id_infracoes).distinct().order_by("tipo"),
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


def gerar_xls(request):
    if request.method == "GET":
        qs = Ocorrencia.objects.all()
        
        id_exato = request.GET.get("id_exato", "")
        infracao = request.GET.get("infracao", "")
        cidade = request.GET.get("cidade", "")
        companhia = request.GET.get("companhia", "")
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
        
        if is_valid_queryparam(cidade):
            qs = qs.filter(endereco__municipio__codigo_ibge=cidade)
            filtro_por_cidade = True
        else:
            filtro_por_cidade = False

        if is_valid_queryparam(companhia):
            qs = qs.filter(guarnicao__companhia=companhia)

        if is_valid_queryparam(data_inicial):
            dinicial = timezone.now().strptime(data_inicial, "%d/%m/%Y")
            qs = qs.filter(dataocorrencia__date__gte=dinicial)

        if is_valid_queryparam(data_final):
            dfinal = timezone.now().strptime(data_final, "%d/%m/%Y")
            qs = qs.filter(dataocorrencia__date__lte=dfinal)

        if envolvidos == "on":
            qs = qs.filter(envolvido_ocorrencia__isnull=False).distinct()
            if is_valid_queryparam(envolvido):
                qs = qs.filter(envolvido_ocorrencia__pessoa__nome__icontains=envolvido)

        if armas == "on":
            qs = qs.filter(
                acessoriosocorrencia_ocorrencia__armaacessorio_acessoriosocorrencia__isnull=False).distinct()

        if diversos == "on":
            qs = qs.filter(
                acessoriosocorrencia_ocorrencia__diversosacessorio_acessoriosocorrencia__isnull=False).distinct()

        if docs == "on":
            qs = qs.filter(
                acessoriosocorrencia_ocorrencia__docacessorio_acessoriosocorrencia__isnull=False).distinct()

        if drogas == "on":
            qs = qs.filter(
                acessoriosocorrencia_ocorrencia__drogaacessorio_acessoriosocorrencia__isnull=False).distinct()

        if municoes == "on":
            qs = qs.filter(
                acessoriosocorrencia_ocorrencia__municaoacessorio_acessoriosocorrencia__isnull=False).distinct()

        if veiculos == "on":
            qs = qs.filter(
                acessoriosocorrencia_ocorrencia__veiculoacessorio_acessoriosocorrencia__isnull=False).distinct()

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename=RELATÓRIO_'+ timezone.localtime().strftime('%d_%m_%Y_%H_%M') +'.xls'

        wb = xlwt.Workbook(encoding='utf8')
        ws = wb.add_sheet('Relatório de Ocorrências', cell_overwrite_ok=True)

        style_heading = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 320;
            align:
                wrap on,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour 0x19;
            """)

        c = 0

        ws.write_merge(0, 0, c, c+1, 'Relatório de Ocorrências', style_heading)

        style_body = xlwt.easyxf("""
            font:
                name Arial,
                bold on,
                height 240;
            align:
                wrap on,
                vert center,
                horiz center;
            """)

        try:
            for i in itertools.count():
                ws.col(i).width = 340 * 20
        except ValueError:
            pass

        menor_data = qs.earliest('dataocorrencia').dataocorrencia
        maior_data = qs.latest('dataocorrencia').dataocorrencia

        ws.write_merge(1, 1, 0, c+1, "Período: " + menor_data.strftime('%d/%m/%Y') + " até " + maior_data.strftime('%d/%m/%Y'), style_body)

        r = 2
        c = 0

        columns_header = ['TIPO PENAL', 'QUANTIDADE']

        for column_index in range(len(columns_header)):
            ws.write(r, column_index, columns_header[column_index], style_body)
        r += 1

        data = qs.values_list('infracao__tipo').annotate(Count('pk')).order_by('infracao__tipo').distinct()
        
        for infracao, qtd in data:
            c = 0
            if not infracao:
                ws.write(r, c, "NÃO HÁ", style_body)
            else:
                ws.write(r, c, infracao, style_body)
            c += 1
            ws.write(r, c, qtd, style_body)
            r += 1

        c = 0
        
        ws.write(r, c, "TOTAL", style_body)
        ws.write(r, c+1, xlwt.Formula("SUM(B3:B" + str(len(data) + 3) + ")"), style_body)

        c = 0
        r += 1

        r += 1

        ws.write_merge(r, r, c, c+1, "Gerado " + timezone.localtime().strftime('%d/%m/%Y %H:%M'), style_body)

        output = io.BytesIO()
        wb.save(output)
        output.seek(0)
        response.write(output.getvalue())
    
        return response


@xframe_options_exempt
def geraemostrapdfocorrencia(request, id):
    try:
        ocorrencia = Ocorrencia.objects.get(id=id)

        if ocorrencia.relatorio:
            pasta = "ocorrencias/"
            nomearquivo = "Ocorrencia_" + str(ocorrencia.id) + "-" +\
                timezone.localtime(ocorrencia.dataocorrencia).strftime("%Y")
            arquivo = pasta + str(nomearquivo + ".pdf").replace(" ", "_")
            
            filename = PDF_ROOT + pasta + str(nomearquivo + ".pdf").replace(" ", "_")

            context_pdf = {
                "ocorrencia": ocorrencia,
                "pms": PolicialViatura.objects.filter(
                    guarnicao=ocorrencia.guarnicao).order_by(
                        "policial__nomeguerra"),
                "envolvidos": Envolvido.objects.filter(
                    ocorrencia=ocorrencia),
                "anexos": Anexo.objects.filter(ocorrencia=ocorrencia),
                "aditamentos": ObservacaoOcorrencia.objects.filter(ocorrencia=ocorrencia)
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

            GerarPDF("pdf/ocorrencia.html", context_pdf, arquivo)

            with open(filename, 'r'):
                response = FileResponse(open(filename))
                return response
        else:
            return redirect("index")

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
