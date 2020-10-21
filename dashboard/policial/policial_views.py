from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.core.paginator import Paginator

# AUTH
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    login,
    authenticate,
    update_session_auth_hash
)
from django.contrib.auth.hashers import check_password

# MODELS
from policial.models import Policial
from contasdeusuario.models import Usuario
from policialviatura.models import PolicialViatura
from opo.models import OPORelatorio
from guarnicao.models import Guarnicao

# FORMS
from .forms import (
    FormRegistrarUsuario,
    FormRegistrarPolicial,
    FormAtualizarEmail,
    FormAtualizarFoto,
    FormAtualizarSenha
)
from django.db.models import Q


@login_required
@csrf_exempt
def atualizar_senha(request):
    if request.is_ajax and request.method == "POST":
        usuario = Usuario.objects.get(id=request.user.id)
        old_pass = request.POST.get("password")
        new_pass1 = request.POST.get("new_password1")
        new_pass2 = request.POST.get("new_password2")

        data = dict()

        if check_password(old_pass, usuario.password):
            if(new_pass1 == old_pass) or (new_pass2 == old_pass):
                data["message"] = "A nova senha não pode ser igual a antiga."
                status = 400
            elif new_pass1 == new_pass2:
                usuario.set_password(new_pass1)
                usuario.save()
                update_session_auth_hash(request, usuario)
                login(request, authenticate(
                    matricula=request.user.matricula, password=new_pass1))
                data["message"] = "Senha alterada com sucesso!"
                status = 200
            else:
                data["message"] = "Nova senha divergente. "\
                                  "Informe novamente a mesma!"
                status = 400
        else:
            data["message"] = "Senha atual incorreta."
            status = 400

        return JsonResponse(data, status=status)


@login_required
@csrf_exempt
def atualizar_foto(request):
    if request.is_ajax and request.method == "POST":
        foto = FormAtualizarFoto(
               request.POST, request.FILES,
               instance=request.user.policial)

        if foto.is_valid():
            foto.save()

        return JsonResponse({"message": "Foto atualizada."}, status=200)


@login_required
@csrf_exempt
def atualizar_email(request):
    if request.is_ajax and request.method == "POST":
        email = FormAtualizarEmail(
                request.POST,
                instance=request.user)

        if email.is_valid():
            email.save()

        return JsonResponse({"message": "E-mail atualizado."}, status=200)


@login_required
def perfil(request):
    context = {
        "policial": get_object_or_404(
                    Policial,
                    matricula_id__matricula=get_object_or_404(
                        Usuario,
                        pk=request.user.id).get_username()),
        "email": FormAtualizarEmail(instance=request.user),
        "foto": FormAtualizarFoto(instance=request.user.policial),
        "senha": FormAtualizarSenha(instance=request.user)
    }

    return render(request, "policial/perfil.html", context)


@login_required
def registrar(request):
    if request.method == "POST":
        registrar_usuario_form = FormRegistrarUsuario(request.POST)
        registrar_policial_form = FormRegistrarPolicial(request.POST)
        if registrar_usuario_form.is_valid()\
                and registrar_policial_form.is_valid():
            usuario = registrar_usuario_form.save()
            policial = registrar_policial_form.save(commit=False)
            policial.matricula = usuario
            policial.save()

            return redirect("policial:listar_policiais")

    context = {
        "registrar_usuario_form": FormRegistrarUsuario(),
        "registrar_policial_form": FormRegistrarPolicial()
        }

    return render(request, "gestao/registrar_policial.html", context)


@login_required
def remover(request, id):
    policial = get_object_or_404(Policial, id=id)
    if request.method == "POST":
        policial.delete()
        return redirect("policial:listar_policiais")
    context = {"policial": policial}

    return render(request, "gestao/remover_policial.html", context)


@login_required
def listar_policiais(request):
    paginador = Paginator(
                get_policiais().order_by("matricula__nome"), 10)
    numero_pagina = request.GET.get("pagina")
    policiais = paginador.get_page(numero_pagina)
    context = {"policiais": policiais}

    return render(request, 'gestao/listar_policiais.html', context)


@login_required
def mostrar(request, id):
    context = {
        "pm": mostrar_policial(id)}

    return render(request, "gestao/mostrar_policial.html", context)


@login_required
def buscar_policial(request, guarnicao):
    if request.is_ajax():
        ids = []
        results = []
        term = request.GET.get("term", None)

        guarnicao = Guarnicao.objects.get(id=guarnicao)

        for z in Guarnicao.objects.filter(ativo=False, datafechamento__isnull=True):
            ids.append(z.comandante.id)

        for y in PolicialViatura.objects.filter(
                guarnicao=guarnicao):
            ids.append(y.policial.id)

        for x in PolicialViatura.objects.filter(
                Q(guarnicao__datafechamento=None, guarnicao__ativo=True) & Q(ativo=True)):
            ids.append(x.policial.id)
        
        policiais = Policial.objects.filter(companhia=guarnicao.companhia)
        policiais = policiais.filter(Q(nomeguerra__icontains=term) | Q(matricula__matricula__icontains=term))

        policiais = policiais.exclude(id__in=ids).order_by("matricula__nome")

        if policiais.count() > 0:
            for policial in policiais:
                policiais_objeto = {
                    "id": policial.id,
                    "nome": "{} - {} {}".format(policial.matricula.matricula, policial.postograduacao, policial.nomeguerra)
                }
                results.append(policiais_objeto)
        else:
            results.append({"id": ""})

        return JsonResponse(results, safe=False)


def mostrar_policial(id):
    policial = Policial.objects.get(id=id)
    return policial


def get_policiais():
    policiais = Policial.objects.all()
    return policiais
