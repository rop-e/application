from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from endereco.models import (
    Municipios,
    Endereco
)
from dashboard.endereco.forms import FormEndereco
from django.http import JsonResponse
from utils.extrair_lat_lng import extract_lat_lng
from ocorrencia.models import (
    Ocorrencia,
    Infracao
)
from django.utils import timezone
from django.http import QueryDict


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Ocorrencia.objects.filter(relatorio__isnull=False)

    infracao = request.GET.get("infracao", "")
    municipio = request.GET.get("municipio", "")
    data_inicial = request.GET.get("data_inicial", "")
    data_final = request.GET.get("data_final", "")

    if is_valid_queryparam(infracao):
        qs = qs.filter(infracao=infracao)

    if is_valid_queryparam(municipio):
        qs = qs.filter(endereco__municipio__codigo_ibge=municipio)

    if is_valid_queryparam(data_inicial):
        dinicial = timezone.now().strptime(data_inicial, "%d/%m/%Y")
        qs = qs.filter(dataocorrencia__date__gte=dinicial)
    else:
        qs = qs.filter(dataocorrencia__date__gte=timezone.now()-timezone.timedelta(days=30))

    if is_valid_queryparam(data_final):
        dfinal = timezone.now().strptime(data_final, "%d/%m/%Y")
        qs = qs.filter(dataocorrencia__date__lte=dfinal)
    else:
        qs = qs.filter(dataocorrencia__date__lte=timezone.now())

    return qs


@login_required
def index(request):
    qs = filter(request)

    infracoes = Infracao.objects.filter(ocorrencia__isnull=False, ocorrencia__relatorio__isnull=False).distinct().order_by("tipo")
    municipios = Municipios.objects.filter(batalhaomunicipios__batalhao__batalhao=request.user.policial.batalhao, endereco__ocorrencia__isnull=False, endereco__ocorrencia__relatorio__isnull=False).distinct().order_by("batalhaomunicipios__municipio__nome")

    filtros = QueryDict(mutable=True)

    if not is_valid_queryparam(request.GET.get("municipio", "")):
        cidade = 2911709
        filtros.appendlist("Cidade", Municipios.objects.get(codigo_ibge=cidade))
    
    if not is_valid_queryparam(request.GET.get("data_inicial", "")):
        filtros.appendlist("Data inicial", timezone.localtime(timezone.now()-timezone.timedelta(days=30)).strftime("%d/%m/%Y"))

    if not is_valid_queryparam(request.GET.get("data_final", "")):
        filtros.appendlist("Data final", timezone.localtime().strftime("%d/%m/%Y"))

    for k, v in request.GET.items():
        if v != "":
            if k == "municipio":
                filtros.appendlist("Cidade", Municipios.objects.get(codigo_ibge=v))
                cidade = v
            elif k == "infracao":
                filtros.appendlist("Infração", Infracao.objects.get(id=v))
            elif k == "data_inicial":
                filtros.appendlist("Data inicial", v)
            elif k == "data_final":
                filtros.appendlist("Data final", v)

    context = {
        "ocorrencias": qs,
        "municipios": municipios,
        "filtros": filtros,
        "infracoes": infracoes,
        "cidade": get_cidade(cidade)
    }

    return render(request, "endereco/mapa.html", context)


@login_required
def edit_endereco(request, id):
    try:
        endereco = Endereco.objects.get(id=id)
        
        context = {
            "id": endereco.id,
            "endereco": FormEndereco(instance=endereco)
        }

        return render(request, "ocorrencia/edits/edit_endereco.html", context)
    except Exception:
        pass


@login_required
def post_edit_endereco(request):
    if request.is_ajax and request.method == "POST":
        instance = Endereco.objects.get(id=request.POST.get("id_endereco"))

        form = FormEndereco(request.POST, instance=instance)

        if form.is_valid():
            endereco = form.save(commit=False)

            if endereco.numero is None:
                numero = ""
            else:
                numero = ", " + endereco.numero

            address = "{}, {}, Rua {}{}".format(
                endereco.municipio, endereco.bairro, endereco.rua, numero)

            geolocalizacao = extract_lat_lng(address)

            endereco.latitude = geolocalizacao[0]
            endereco.longitude = geolocalizacao[1]

            endereco.save()

            return JsonResponse(
                {"message": "Endereço atualizado."}, status=200)
        else:
            return JsonResponse(form.errors, status=400)


def get_cidade(codigo_ibge):
    cidade = Municipios.objects.get(codigo_ibge=codigo_ibge)
    latitude = cidade.latitude
    longitude = cidade.longitude
    return "{}, {}".format(latitude, longitude)

