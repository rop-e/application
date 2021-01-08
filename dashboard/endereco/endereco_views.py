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
from django.http import QueryDict


@login_required
def index(request):

    id_infracoes = []

    cidade = request.GET.get("municipio", None)
    infracao = request.GET.get("infracao", None)

    for ocorrencia in Ocorrencia.objects.all():
        id_infracoes.append(ocorrencia.infracao.id)

    filtros = QueryDict(mutable=True)

    for k, v in request.GET.items():
        if v != "":
            if k == "municipio":
                filtros.appendlist("Cidade", Municipios.objects.get(codigo_ibge=v))
            if k == "infracao":
                filtros.appendlist("Infração", Infracao.objects.get(id=v))

    context = {
        "cidade": get_cidade(cidade),
        "municipios": Municipios.objects.filter(
            batalhaomunicipios__batalhao__batalhao=request.user.policial.batalhao).order_by(
                "batalhaomunicipios__municipio__nome"),
        "filtros": filtros,
        "coordenadas": get_coordenadas(query(cidade, infracao)),
        "qtd": query(cidade, infracao).count(),
        "infracoes": Infracao.objects.filter(id__in=id_infracoes),
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


def get_municipios():
    municipios = Municipios.objects.all().order_by("nome")
    return municipios


def get_cidade(codigo_ibge):
    if codigo_ibge == "" or codigo_ibge is None:
        codigo_ibge = 2911709

    cidade = Municipios.objects.get(codigo_ibge=codigo_ibge)
    latitude = cidade.latitude
    longitude = cidade.longitude
    return "{}, {}".format(latitude, longitude)


def query(cidade, infracao):
    if cidade == "" or cidade is None:
        cidade = 2911709

    if infracao:
        return Endereco.objects.filter(
        ocorrencia__isnull=False,
        municipio__codigo_ibge=cidade, ocorrencia__infracao=infracao)
    else:
        return Endereco.objects.filter(
        ocorrencia__isnull=False,
        municipio__codigo_ibge=cidade)



def get_coordenadas(qs):
    coordenadas = []

    for coordenada in qs:
        coordenadas.append([
            float(coordenada.latitude),
            float(coordenada.longitude)
        ])

    return coordenadas
