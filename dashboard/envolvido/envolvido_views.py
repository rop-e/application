from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from envolvido.serializers import (
    EnvolvidoSerializer,
    ListEnvolvidoSerializer
)

# MODELS
from envolvido.models import Envolvido
from pessoa.models import Pessoa

# FORMS
from .forms import (
    FormEnvolvido,
    FormEnvolvidoRAT,
    FormEditarEnvolvidoOcorrencia,
    FormEditarEnvolvidoRAT
)
from dashboard.localrecebedor.forms import FormEnvolvidoAgenteRecebedor
from dashboard.pessoa.forms import FormPessoa
from dashboard.rat.forms import FormRATVeiculoEnvolvidos
from rat.models import RATVeiculoEnvolvidos
import json
from dashboard.observacao.forms import FormObservacao
from rat.serializers import ListRATVeiculoEnvolvidosSerializer


@login_required
def get_envolvidos(request):
    ocorrencia = request.GET.get("ocorrencia", None)
    
    data = dict()

    if ocorrencia is not None:
        envolvidos = Envolvido.objects.filter(
            ocorrencia=ocorrencia).order_by("-id")

    if envolvidos:
        serializer = ListEnvolvidoSerializer(envolvidos, many=True)
        data["envolvidos"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def get_envolvidosrat(request):
    try:
        rat = request.GET.get("rat", None)
        veiculo = RATVeiculoEnvolvidos.objects.filter(envolvido__rat=rat)
        envolvidossemveiculo = Envolvido.objects.filter(ratveiculoenvolvidos__envolvido__isnull=True, rat=rat)
    except Exception:
        pass

    data = dict()

    if envolvidossemveiculo:
        serializador_envolvido = ListEnvolvidoSerializer(envolvidossemveiculo, many=True)
        data["envolvidossemveiculo"] = list(serializador_envolvido.data)
    if veiculo:
        serializer = ListRATVeiculoEnvolvidosSerializer(veiculo, many=True)
        data["veiculoenvolvidos"] = list(serializer.data)

    return JsonResponse(data)


@login_required
@csrf_exempt
def post_envolvidoocorrencia(request):
    if request.is_ajax and request.method == "POST":
        id_pessoa = request.POST.get("id_pessoa")
        pessoa = FormPessoa(request.POST or None)
        envolvido = FormEnvolvido(
                    request.POST or None)
        agenterecebedor = FormEnvolvidoAgenteRecebedor(
                          request.POST or None)

        if id_pessoa:
            if envolvido.is_valid():
                envolvido = envolvido.save(commit=False)
                envolvido.pessoa = Pessoa.objects.get(id=id_pessoa)

                if agenterecebedor.is_valid():
                    envolvido.agenterecebedor = agenterecebedor.save()
            else:
                return JsonResponse(envolvido.errors, status=400)
        else:
            if pessoa.is_valid()\
                    and envolvido.is_valid():
                envolvido = envolvido.save(commit=False)
                envolvido.pessoa = pessoa.save()

                if agenterecebedor.is_valid():
                    envolvido.agenterecebedor = agenterecebedor.save()
            else:
                return JsonResponse({"pessoa": pessoa.errors, "envolvido": envolvido.errors}, status=400)

        envolvido.save()

        instance = EnvolvidoSerializer(envolvido).data
        return JsonResponse({"instance": instance}, status=200)


@login_required
@csrf_exempt
def post_envolvidorat(request):
    if request.is_ajax and request.method == "POST":
        id_pessoa = request.POST.get("id_pessoa")
        pessoa = FormPessoa(request.POST or None)
        envolvido = FormEnvolvidoRAT(request.POST or None)
        agenterecebedor = FormEnvolvidoAgenteRecebedor(request.POST or None)
        ratveiculoenvolvidos = FormRATVeiculoEnvolvidos(request.POST or None)
        versao = FormObservacao(request.POST or None)

        if id_pessoa:
            if envolvido.is_valid():
                envolvido = envolvido.save(commit=False)
                envolvido.pessoa = Pessoa.objects.get(id=id_pessoa)

                if agenterecebedor.is_valid():
                    envolvido.agenterecebedor = agenterecebedor.save()
            else:
                return JsonResponse(envolvido.errors, status=400)
        else:
            if pessoa.is_valid()\
                    and envolvido.is_valid():
                envolvido = envolvido.save(commit=False)
                envolvido.pessoa = pessoa.save()

                if agenterecebedor.is_valid():
                    envolvido.agenterecebedor = agenterecebedor.save()
            else:
                return JsonResponse({"pessoa": pessoa.errors, "envolvido": envolvido.errors}, status=400)

        if ratveiculoenvolvidos.is_valid():
            ratveiculoenvolvidos = ratveiculoenvolvidos.save(commit=False)

            if envolvido.tipoenvolvimento.tipo == "CONDUTOR":
                if RATVeiculoEnvolvidos.objects.filter(
                        ratveiculos=ratveiculoenvolvidos.ratveiculos,
                        envolvido__tipoenvolvimento__tipo="CONDUTOR").exists():

                    data = {
                        "ratveiculoenvolvidos": {
                            "error": "Você já inseriu o condutor deste veículo!"
                        }
                    }
                    return JsonResponse(data, safe=False, status=400)
        
            envolvido.observacao = versao.save()
            envolvido.save()

            ratveiculoenvolvidos.envolvido = envolvido
            ratveiculoenvolvidos.save()
        else:
            envolvido.observacao = versao.save()
            envolvido.save()

        instance = EnvolvidoSerializer(envolvido).data
        return JsonResponse({"instance": instance}, status=200)


@login_required
def checar_nome_existente(request):
    if request.is_ajax and request.method == "GET":
        nome = request.GET.get("nome", None)
        ocorrencia = request.GET.get("ocorrencia", None)
        rat = request.GET.get("rat", None)

        envolvido = Envolvido.objects.filter(pessoa__nome=nome)

        if ocorrencia is not None:
            envolvido = envolvido.filter(ocorrencia=ocorrencia)

            if envolvido.exists():
                return JsonResponse({"invalid": True}, status=200)
        elif rat is not None:
            envolvido = envolvido.filter(rat=rat)

            if envolvido.exists():
                return JsonResponse({"invalid": True}, status=200)
    
    return JsonResponse({}, status=200)


@login_required
def edit_envolvido_ocorrencia(request, id):
    try:
        envolvido = Envolvido.objects.get(id=id)

        context = {
            "id": envolvido.id,
            "envolvido": FormEditarEnvolvidoOcorrencia(instance=envolvido),
            "pessoa": FormPessoa(instance=envolvido.pessoa)
        }

        return render(request, "ocorrencia/edits/edit_envolvido.html", context)
    except Exception:
        pass


@login_required
def edit_envolvido_rat(request, id):
    try:
        envolvido = Envolvido.objects.get(id=id)

        context = {
            "id": envolvido.id,
            "envolvido": FormEditarEnvolvidoRAT(instance=envolvido),
            "pessoa": FormPessoa(instance=envolvido.pessoa)
        }

        return render(request, "rat/edits/edit_envolvido.html", context)
    except Exception:
        pass


@login_required
def post_edit_envolvidoocorrencia(request):
    if request.is_ajax and request.method == "POST":
        instance = Envolvido.objects.get(id=request.POST.get("id_envolvido"))

        envolvido = FormEditarEnvolvidoOcorrencia(request.POST, instance=instance)
        pessoa = FormPessoa(request.POST, instance=instance.pessoa)

        if pessoa.is_valid()\
                and envolvido.is_valid():
            pessoa.save()
            envolvido.save()

            return JsonResponse(
                {"message": "Envolvido atualizado."}, status=200)
        else:
            return JsonResponse({
                "pessoa": pessoa.errors,
                "envolvido": envolvido.errors
            }, status=400)


@login_required
def post_edit_envolvidorat(request):
    if request.is_ajax and request.method == "POST":
        instance = Envolvido.objects.get(id=request.POST.get("id_envolvido"))

        envolvido = FormEditarEnvolvidoRAT(request.POST, instance=instance)
        pessoa = FormPessoa(request.POST, instance=instance.pessoa)

        if pessoa.is_valid()\
                and envolvido.is_valid():
            pessoa.save()
            envolvido.save()

            return JsonResponse(
                {"message": "Envolvido atualizado."}, status=200)
        else:
            return JsonResponse({
                "pessoa": pessoa.errors,
                "envolvido": envolvido.errors
            }, status=400)


@login_required
@csrf_exempt
def delete_envolvido(request):
    if request.is_ajax and request.method == "POST":
        data = dict()
        id = request.POST.get("id")
        envolvido = Envolvido.objects.get(id=id)

        if envolvido:
            envolvido.delete()
            data["message"] = "Envolvido removido."
        else:
            data["message"] = "Erro!"

        return JsonResponse(data)
