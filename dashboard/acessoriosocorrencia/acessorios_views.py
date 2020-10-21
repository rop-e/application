from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# MODELS
from acessoriosocorrencia.models import (
    Arma,
    ArmaAcessorio,
    DiversosAcessorio,
    DocAcessorio,
    DrogaAcessorio,
    MunicaoAcessorio,
    VeiculoAcessorio
)
from veiculo.models import Veiculo

# SERIALIZERS
from acessoriosocorrencia.serializers import (
    ArmaAcessorioSerializer,
    DiversosAcessorioSerializer,
    DocAcessorioSerializer,
    DrogaAcessorioSerializer,
    MunicaoAcessorioSerializer,
    VeiculoAcessorioSerializer,
    ListArmaAcessorioSerializer,
    ListDiversosAcessorioSerializer,
    ListDocAcessorioSerializer,
    ListDrogaAcessorioSerializer,
    ListMunicaoAcessorioSerializer,
    ListVeiculoAcessorioSerializer
)

# FORMS
from dashboard.veiculo.forms import FormVeiculo
from .forms import (
    FormArma,
    FormArmaAcessorio,
    FormDrogaAcessorio,
    FormEditarDrogaAcessorio,
    FormDiversosAcessorio,
    FormEditarDiversosAcessorio,
    FormDocAcessorio,
    FormEditarDocAcessorio,
    FormMunicaoAcessorio,
    FormEditarMunicaoAcessorio,
    FormVeiculoAcessorio
)
from dashboard.localrecebedor.forms import FormAcessorioAgenteRecebedor
from dashboard.observacao.forms import FormObservacao


# ARMAS
@login_required
def get_armas(request):
    try:
        acessoriosocorrencia = request.GET.get("acessoriosocorrencia")
        armas = ArmaAcessorio.objects.filter(
            acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
    except Exception as error:
        raise error

    data = dict()

    if armas:
        serializer = ListArmaAcessorioSerializer(armas, many=True)
        data["armas"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_arma(request):
    if request.is_ajax and request.method == "POST":
        arma = FormArma(request.POST or None)
        armaacessorio = FormArmaAcessorio(request.POST or None)
        agenterecebedor = FormAcessorioAgenteRecebedor(
                          request.POST or None)
        observacao = FormObservacao(request.POST or None)

        if arma.is_valid()\
            and armaacessorio.is_valid()\
                and agenterecebedor.is_valid():
            arma = arma.save()
            agenterecebedor = agenterecebedor.save()

            armaacessorio = armaacessorio.save(commit=False)
            armaacessorio.arma = arma
            armaacessorio.agenterecebedor = agenterecebedor

            if observacao.is_valid():
                armaacessorio.observacao = observacao.save()

            armaacessorio.save()

            instance = ArmaAcessorioSerializer(armaacessorio).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse({
                        "arma": arma.errors,
                        "armaacessorio": armaacessorio.errors
                    }, status=400)


@login_required
def checar_numero_serie_existente(request):
    if request.is_ajax and request.method == "GET":
        numeroserie = request.GET.get("numeroserie", None)
        acessoriosocorrencia = request.GET.get("acessoriosocorrencia")

        if ArmaAcessorio.objects.filter(
                arma__numeroserie=numeroserie,
                acessoriosocorrencia=acessoriosocorrencia).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=200)


@login_required
def edit_arma(request, id):
    try:
        arma = Arma.objects.get(id=id)

        context = {
            "id": arma.id,
            "arma": FormArma(instance=arma)
        }

        return render(request, "ocorrencia/edits/edit_arma.html", context)
    except Exception:
        pass


@login_required
def post_edit_arma(request):
    if request.is_ajax and request.method == "POST":
        instance = Arma.objects.get(id=request.POST.get("id_arma"))

        arma = FormArma(request.POST, instance=instance)

        if arma.is_valid():
            arma.save()

            return JsonResponse({"message": "Arma atualizada."}, status=200)
        else:
            return JsonResponse(arma.errors, status=400)


@login_required
@csrf_exempt
def delete_arma(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            arma = Arma.objects.get(id=id)

            data = dict()

            if arma:
                arma.delete()
                data["message"] = "Arma removida."

            return JsonResponse(data)
        except Exception as error:
            raise error


# DROGAS
@login_required
def get_drogas(request):
    try:
        acessoriosocorrencia = request.GET.get("acessoriosocorrencia")
        drogas = DrogaAcessorio.objects.filter(
            acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
    except Exception as error:
        raise error

    data = dict()

    if drogas:
        serializer = ListDrogaAcessorioSerializer(drogas, many=True)
        data["drogas"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_droga(request):
    if request.is_ajax and request.method == "POST":
        drogaacessorio = FormDrogaAcessorio(request.POST or None)
        agenterecebedor = FormAcessorioAgenteRecebedor(request.POST or None)
        observacao = FormObservacao(request.POST or None)

        if drogaacessorio.is_valid()\
                and agenterecebedor.is_valid():
            agenterecebedor = agenterecebedor.save()

            drogaacessorio = drogaacessorio.save(commit=False)
            drogaacessorio.agenterecebedor = agenterecebedor

            if observacao.is_valid():
                drogaacessorio.observacao = observacao.save()

            drogaacessorio.save()

            instance = DrogaAcessorioSerializer(drogaacessorio).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse(drogaacessorio.errors, status=400)

    return JsonResponse({"error": ""}, status=400)


@login_required
def edit_droga(request, id):
    try:
        droga = DrogaAcessorio.objects.get(id=id)

        context = {
            "id": droga.id,
            "droga": FormEditarDrogaAcessorio(instance=droga)
        }

        return render(request, "ocorrencia/edits/edit_droga.html", context)
    except Exception:
        pass


@login_required
def post_edit_droga(request):
    if request.is_ajax and request.method == "POST":
        instance = DrogaAcessorio.objects.get(id=request.POST.get("id_droga"))

        droga = FormEditarDrogaAcessorio(request.POST, instance=instance)

        if droga.is_valid():
            droga.save()

            return JsonResponse({"message": "Droga atualizada."}, status=200)
        else:
            return JsonResponse(droga.errors, status=400)


@login_required
@csrf_exempt
def delete_droga(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            drogaacessorio = DrogaAcessorio.objects.get(id=id)

            data = dict()

            if drogaacessorio:
                drogaacessorio.delete()
                data["message"] = "Droga removida."

            return JsonResponse(data)
        except Exception as error:
            raise error


# DIVERSOS
@login_required
def get_diversos(request):
    try:
        acessoriosocorrencia = request.GET.get("acessoriosocorrencia")
        diversos = DiversosAcessorio.objects.filter(
            acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
    except Exception as error:
        raise error

    data = dict()

    if diversos:
        serializer = ListDiversosAcessorioSerializer(diversos, many=True)
        data["diversos"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_diverso(request):
    if request.is_ajax and request.method == "POST":
        diversosacessorio = FormDiversosAcessorio(
                            request.POST or None)
        agenterecebedor = FormAcessorioAgenteRecebedor(
                          request.POST or None)
        observacao = FormObservacao(request.POST or None)

        if diversosacessorio.is_valid()\
                and agenterecebedor.is_valid():
            agenterecebedor = agenterecebedor.save()

            diversosacessorio = diversosacessorio.save(commit=False)
            diversosacessorio.agenterecebedor = agenterecebedor

            if observacao.is_valid():
                diversosacessorio.observacao = observacao.save()

            diversosacessorio.save()

            instance = DiversosAcessorioSerializer(diversosacessorio).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse(diversosacessorio.errors, status=400)

    return JsonResponse({"error": ""}, status=400)


@login_required
def edit_diverso(request, id):
    try:
        diverso = DiversosAcessorio.objects.get(id=id)

        context = {
            "id": diverso.id,
            "diverso": FormEditarDiversosAcessorio(instance=diverso)
        }

        return render(request, "ocorrencia/edits/edit_diverso.html", context)
    except Exception:
        pass


@login_required
def post_edit_diverso(request):
    if request.is_ajax and request.method == "POST":
        instance = DiversosAcessorio.objects.get(
            id=request.POST.get("id_diverso"))

        diverso = FormEditarDiversosAcessorio(request.POST, instance=instance)

        if diverso.is_valid():
            diverso.save()

            return JsonResponse({"message": "Objeto atualizado."}, status=200)
        else:
            return JsonResponse(diverso.errors, status=400)


@login_required
@csrf_exempt
def delete_diverso(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            diversoacessorio = DiversosAcessorio.objects.get(id=id)

            data = dict()

            if diversoacessorio:
                diversoacessorio.delete()
                data["message"] = "Item removido."

            return JsonResponse(data)
        except Exception as error:
            raise error


# DOCUMENTOS
@login_required
def get_docs(request):
    try:
        acessoriosocorrencia = request.GET.get("acessoriosocorrencia")
        docs = DocAcessorio.objects.filter(
            acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
    except Exception as error:
        raise error

    data = dict()

    if docs:
        serializer = ListDocAcessorioSerializer(docs, many=True)
        data["docs"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_doc(request):
    if request.is_ajax and request.method == "POST":
        docacessorio = FormDocAcessorio(request.POST or None)
        agenterecebedor = FormAcessorioAgenteRecebedor(
                          request.POST or None)
        observacao = FormObservacao(request.POST or None)

        if docacessorio.is_valid()\
                and agenterecebedor.is_valid():
            agenterecebedor = agenterecebedor.save()

            docacessorio = docacessorio.save(commit=False)
            docacessorio.agenterecebedor = agenterecebedor

            if observacao.is_valid():
                docacessorio.observacao = observacao.save()

            docacessorio.save()

            instance = DocAcessorioSerializer(docacessorio).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse({"error": docacessorio.errors}, status=400)

    return JsonResponse({"error": ""}, status=400)


@login_required
def checar_numero_existente(request):
    if request.is_ajax and request.method == "GET":
        numero = request.GET.get("numero", None)
        acessoriosocorrencia = request.GET.get("acessoriosocorrencia")

        if DocAcessorio.objects.filter(
                numero=numero,
                acessoriosocorrencia=acessoriosocorrencia).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)


@login_required
def edit_doc(request, id):
    try:
        doc = DocAcessorio.objects.get(id=id)

        context = {
            "id": doc.id,
            "doc": FormEditarDocAcessorio(instance=doc)
        }

        return render(request, "ocorrencia/edits/edit_documento.html", context)
    except Exception:
        pass


@login_required
def post_edit_doc(request):
    if request.is_ajax and request.method == "POST":
        instance = DocAcessorio.objects.get(id=request.POST.get("id_doc"))

        doc = FormEditarDocAcessorio(request.POST, instance=instance)

        if doc.is_valid():
            doc.save()

            return JsonResponse(
                {"message": "Documento atualizado."}, status=200)
        else:
            return JsonResponse(doc.errors, status=400)


@login_required
@csrf_exempt
def delete_doc(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            docacessorio = DocAcessorio.objects.get(id=id)

            data = dict()

            if docacessorio:
                docacessorio.delete()
                data["message"] = "Documento removido."

            return JsonResponse(data)
        except Exception as error:
            raise error


# MUNIÇÕES
@login_required
def get_municoes(request):
    try:
        acessoriosocorrencia = request.GET.get("acessoriosocorrencia")
        municoes = MunicaoAcessorio.objects.filter(
            acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
    except Exception as error:
        raise error

    data = dict()

    if municoes:
        serializer = ListMunicaoAcessorioSerializer(municoes, many=True)
        data["municoes"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_municao(request):
    if request.is_ajax and request.method == "POST":
        municaoacessorio = FormMunicaoAcessorio(request.POST or None)
        agenterecebedor = FormAcessorioAgenteRecebedor(
                          request.POST or None)
        observacao = FormObservacao(request.POST or None)

        if municaoacessorio.is_valid()\
                and agenterecebedor.is_valid():
            agenterecebedor = agenterecebedor.save()

            municaoacessorio = municaoacessorio.save(commit=False)
            municaoacessorio.agenterecebedor = agenterecebedor

            if observacao.is_valid():
                municaoacessorio.observacao = observacao.save()

            municaoacessorio.save()

            instance = MunicaoAcessorioSerializer(municaoacessorio).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse(municaoacessorio.errors, status=400)

    return JsonResponse({"error": ""}, status=400)


@login_required
def edit_municao(request, id):
    try:
        municao = MunicaoAcessorio.objects.get(id=id)

        context = {
            "id": municao.id,
            "municao": FormEditarMunicaoAcessorio(instance=municao)
        }

        return render(request, "ocorrencia/edits/edit_municao.html", context)
    except Exception:
        pass


@login_required
def post_edit_municao(request):
    if request.is_ajax and request.method == "POST":
        instance = MunicaoAcessorio.objects.get(
            id=request.POST.get("id_municao"))

        municao = FormEditarMunicaoAcessorio(request.POST, instance=instance)

        if municao.is_valid():
            municao.save()

            return JsonResponse({"message": "Munição atualizada."}, status=200)
        else:
            return JsonResponse(municao.errors, status=400)


@login_required
@csrf_exempt
def delete_municao(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("id")
            municaoacessorio = MunicaoAcessorio.objects.get(id=id)

            data = dict()

            if municaoacessorio:
                municaoacessorio.delete()
                data["message"] = "Munição removida."

            return JsonResponse(data)
        except Exception as error:
            raise error


# VEÍCULOS
@login_required
def get_veiculos(request):
    try:
        acessoriosocorrencia = request.GET.get("acessoriosocorrencia")
        veiculos = VeiculoAcessorio.objects.filter(
            acessoriosocorrencia=acessoriosocorrencia).order_by("-id")
    except Exception as error:
        raise error

    data = dict()

    if veiculos:
        serializer = ListVeiculoAcessorioSerializer(
            veiculos, many=True)
        data["veiculos"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_veiculo(request):
    if request.is_ajax and request.method == "POST":
        veiculo = FormVeiculo(request.POST or None)
        veiculoacessorio = FormVeiculoAcessorio(
                                     request.POST or None)
        agenterecebedor = FormAcessorioAgenteRecebedor(
                          request.POST or None)
        observacao = FormObservacao(request.POST or None)

        if veiculo.is_valid()\
            and veiculoacessorio.is_valid()\
                and agenterecebedor.is_valid():

            veiculoacessorio = veiculoacessorio.save(
                               commit=False)
            veiculoacessorio.veiculo = veiculo.save()
            veiculoacessorio.agenterecebedor = agenterecebedor.save()

            if observacao.is_valid():
                veiculoacessorio.observacao = observacao.save()
            veiculoacessorio.save()

            instance = VeiculoAcessorioSerializer(
                       veiculoacessorio).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse({
                "veiculo": veiculo.errors,
                "veiculoacessorio": veiculoacessorio.errors
            }, status=400)

    return JsonResponse({"error": ""}, status=400)


@login_required
def checar_veiculo_placa_existente(request):
    if request.is_ajax and request.method == "GET":
        placa = request.GET.get("placa", None)
        acessoriosocorrencia = request.GET.get("acessoriosocorrencia")

        if VeiculoAcessorio.objects.filter(
                veiculo__placa=placa,
                acessoriosocorrencia=acessoriosocorrencia).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)


@login_required
def checar_veiculo_chassi_existente(request):
    if request.is_ajax and request.method == "GET":
        chassi = request.GET.get("chassi", None)
        acessoriosocorrencia = request.GET.get("acessoriosocorrencia")

        if VeiculoAcessorio.objects.filter(
                veiculo__chassi=chassi,
                acessoriosocorrencia=acessoriosocorrencia).exists():
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
