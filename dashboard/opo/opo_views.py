from django.shortcuts import (
    render,
    redirect
)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from opo.models import (
    OPO,
    OPORelatorio,
    OPOComandantesCIA
)
from policial.models import Policial
from guarnicao.models import Guarnicao
from dashboard.guarnicao.guarnicao_views import (
    verifica_guarnicao_ativa,
    get_guarnicao,
    get_guarnicoes
)
from django.core.paginator import Paginator
from dashboard.opo.forms import (
    FormOPO,
    FormCreateOPORelatorio,
    FormCreateOPOComandantesCIA,
    FormCPOEditSubOPO,
    FormEditOPORelatorio
)
from policial.models import Policial
from dashboard.observacao.forms import FormObservacao
from django.http import JsonResponse
from django.urls import reverse
from django.utils import timezone
from opo.serializers import (
    ListOPORelatorioSerializer,
    ListOPOComandantesCIASerializer
)
from django.http import QueryDict

STATUS_RELATORIO = (
    ("pendente", "PENDENTE"),
    ("andamento", "EM ANDAMENTO"),
    ("finalizada", "FINALIZADA")
)


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = OPO.objects.all()

    numeroopo = request.GET.get("numeroopo", "")
    status = request.GET.get("status", "")
    datainicio = request.GET.get("datainicio", "")
    datatermino = request.GET.get("datatermino", "")

    if is_valid_queryparam(numeroopo):
        qs = qs.filter(numeroopo=numeroopo)
    
    if is_valid_queryparam(status):
        qs = qs.filter(oporelatorio__status=status).distinct()

    if is_valid_queryparam(datainicio):
        dinicio = timezone.now().strptime(datainicio, "%d/%m/%Y")
        qs = qs.filter(datainicio__date__gte=dinicio)

    if is_valid_queryparam(datatermino):
        dtermino = timezone.now().strptime(datatermino, "%d/%m/%Y")
        qs = qs.filter(datatermino__date__lte=dtermino)

    if request.user.policial.cargo.cargo == "COORDENADOR DE ÁREA":
        qs = qs.filter(designado="coordenadordearea")
    elif request.user.policial.cargo.cargo == "CICOM":
        qs = qs.filter(designado="cicom")
    elif request.user.policial.companhia.comandante == request.user.policial:
        qs = qs.filter(
            designado="comandantecia",
            opocomandantescia__comandante=request.user.policial)

    return qs


@login_required
def listar(request):
    qs = filter(request)

    numero_pagina = request.GET.get("pagina", "")

    paginador = Paginator(qs.order_by("-id"), 4)

    filtros = QueryDict(mutable=True)

    for k, v in request.GET.items():
        if v != "":
            if k == "numeroopo":
                filtros.appendlist("Número OPO", v)
            elif k == "status":
                if v == "pendente":
                    v = "PENDENTE"
                elif v == "andamento":
                    v = "EM ANDAMENTO"
                elif v == "finalizada":
                    v = "FINALIZADA"

                filtros.appendlist("Status", v)
            elif k == "datainicio":
                filtros.appendlist("Data de ínicio", v)
            elif k == "datatermino":
                filtros.appendlist("Data de término", v)

    context = {
        "opos": paginador.get_page(numero_pagina),
        "status": STATUS_RELATORIO,
        "filtros": filtros,
    }

    return render(request, "opo/listar.html", context)


def filter_policial(request):
    qs = OPORelatorio.objects.filter(
        guarnicao=get_guarnicao(request.user.policial.id))
    status = request.GET.get("status", "")
    
    if is_valid_queryparam(status):
        qs = qs.filter(status=status)

    return qs


@login_required
def listar_policial(request):
    qs = filter_policial(request)

    numero_pagina = request.GET.get("pagina", "")

    paginador = Paginator(qs.order_by("-id"), 4)

    filtros = QueryDict(mutable=True)

    for k, v in request.GET.items():
        if v != "":
            if k == "status":
                if v == "pendente":
                    v = "PENDENTES"
                elif v == "andamento":
                    v = "EM ANDAMENTO"

                filtros.appendlist("", v)

    context = {
        "opos": paginador.get_page(numero_pagina),
        "filtros": filtros
    }
    return render(request, "opo/listar_policial.html", context)


@login_required
def adicionar_opo(request):
    context = {
        "opo": FormOPO(),
        "observacao": FormObservacao()
    }

    return render(request, "opo/adicionar_opo.html", context)


from dashboard.opo.forms import FormDadosOPO, FormSolicitacaoOPO

@login_required
def edit_dadosopo(request, id):
    try:
        opo = OPO.objects.get(id=id)

        context = {
            "id": opo.id,
            "opo": FormDadosOPO(instance=opo)
        }

        return render(request, "opo/edits/edit_dadosopo.html", context)
    except Exception:
        pass


@login_required
def post_edit_dadosopo(request):
    if request.is_ajax and request.method == "POST":
        instance = OPO.objects.get(id=request.POST.get("id_opo"))

        opo = FormDadosOPO(request.POST, instance=instance)

        if opo.is_valid():
            opo.save()

            return JsonResponse(
                {"message": "OPO atualizada."}, status=200)
        else:
            return JsonResponse(opo.errors, status=400)


@login_required
def edit_dadossolicitacaoopo(request, id):
    try:
        opo = OPO.objects.get(id=id)

        context = {
            "id": opo.id,
            "objeto": opo,
            "opo": FormSolicitacaoOPO(instance=opo)
        }

        return render(request, "opo/edits/edit_dadossolicitacao.html", context)
    except Exception:
        pass


@login_required
def post_edit_dadossolicitacaoopo(request):
    if request.is_ajax and request.method == "POST":
        instance = OPO.objects.get(id=request.POST.get("id_opo"))

        opo = FormSolicitacaoOPO(request.POST, instance=instance)

        if opo.is_valid():
            opo.save()

            return JsonResponse(
                {"message": "OPO atualizada."}, status=200)
        else:
            return JsonResponse(opo.errors, status=400)


@login_required
def edit_observacaoopo(request, id):
    try:
        opo = OPO.objects.get(id=id)

        context = {"opo": opo}

        return render(request, "opo/edits/edit_observacao.html", context)
    except Exception:
        pass

from observacao.models import Observacao

@login_required
def post_edit_observacaoopo(request):
    if request.is_ajax and request.method == "POST":
        instance = Observacao.objects.get(id=request.POST.get("id_observacao"))
        observacao = request.POST.get("observacao", None)

        instance.observacao = observacao
        instance.save()

        return JsonResponse(
            {"message": "Observação da OPO atualizada."}, status=200)
    else:
        return JsonResponse({}, status=400)


@login_required
def visualizar_opo(request, id):
    opo = OPO.objects.get(id=id)
    oporelatorios = OPORelatorio.objects.filter(opo=opo)

    context = {
        "opo": opo,
        "timezone": timezone.now(),
        "oporelatorio": FormCreateOPORelatorio(),
        "subopos": oporelatorios
    }
    
    if opo.designado == "comandantecia":
        context["comandantescia"] = OPOComandantesCIA.objects.filter(opo=opo)

    return render(request, "opo/visualizar_opo.html", context)


@login_required
def visualizar_oporelatorio(request, id):
    oporelatorio = OPORelatorio.objects.get(id=id)

    context = {
        "oporelatorio": oporelatorio,
        "guarnicao_ativa": get_guarnicao(request.user.policial.id)
    }

    return render(request, "opo/visualizar_oporelatorio.html", context)


@login_required
def post_opo(request):
    if request.is_ajax and request.method == "POST":
        opo = FormOPO(request.POST or None)
        observacao = FormObservacao(request.POST or None)

        response = dict()

        if opo.is_valid():
            opo = opo.save(commit=False)

            if observacao.is_valid():
                opo.observacao = observacao.save()

            opo.save()

            if opo.designado == "comandantecia":
                response["redirect"] = reverse(
                    "opo:seleciona_comandantescia",
                    kwargs={"opo": opo.id})
            else:
                response["redirect"] = reverse(
                    "opo:cria_oporelatorio",
                    kwargs={"opo": opo.id})
            
            if opo.datatermino:
                inicio = opo.datainicio
                termino = opo.datatermino

                intervalo_datas = [inicio + timezone.timedelta(days=x) for x in range(0, (termino-inicio).days)]

                for data in intervalo_datas:
                    OPORelatorio.objects.create(
                        opo=opo,
                        local=opo.local,
                        dataexecucao=data,
                        datafinalizacao=
                        data + timezone.timedelta(days=1))
            else:
                OPORelatorio.objects.create(
                    opo=opo,
                    local=opo.local,
                    dataexecucao=opo.datainicio)

            return JsonResponse(response, safe=False, status=200)
        else:
            return JsonResponse(opo.errors, status=400)

    return JsonResponse({"error": ""}, status=400)


@login_required
@csrf_exempt
def post_delete_opo(request):
    if request.is_ajax and request.method == "POST":
        try:
            id = request.POST.get("opo")
            opo = OPO.objects.get(id=id)

            if opo:
                opo.delete()

            return JsonResponse({"redirect": reverse("opo:listar")}, status=200)
        except Exception:
            pass


@login_required
def seleciona_comandantescia(request, opo):
    if request.method == "POST":
        pass

    opo = OPO.objects.get(id=opo)

    context = {
        "opo": opo,
        "form": FormCreateOPOComandantesCIA()
    }

    return render(request, "opo/seleciona_comandantescia.html", context)


@login_required
def post_comandantecia(request):
    if request.is_ajax and request.method == "POST":
        comandantecia = FormCreateOPOComandantesCIA(request.POST or None)

        if comandantecia.is_valid():
            comandantecia = comandantecia.save(commit=False)

            if OPOComandantesCIA.objects.filter(
                    opo=comandantecia.opo,
                    comandante=comandantecia.comandante).exists():
                return JsonResponse({"error": "Você já inseriu esse comandante!"}, status=400)
            else:
                comandantecia.save()

            instance = ListOPOComandantesCIASerializer(comandantecia).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse(comandantecia.errors, status=400)


@login_required
@csrf_exempt
def delete_comandantecia(request):
    if request.is_ajax and request.method == "POST":
        data = dict()
        id = request.POST.get("id")
        comandantecia = OPOComandantesCIA.objects.get(id=id)

        if comandantecia:
            comandantecia.delete()
            data["message"] = "Comandante de CIA removido."
        else:
            data["message"] = "Erro!"

        return JsonResponse(data)


@login_required
def get_comandantescia(request):
    id = request.GET.get("opo", None)
    opocomandantes = OPOComandantesCIA.objects.filter(
        opo__id=id).order_by("-id")

    data = dict()

    if opocomandantes:
        serializer = ListOPOComandantesCIASerializer(opocomandantes, many=True)
        data["comandantescia"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def cria_oporelatorio(request, opo):
    if request.method == "POST":
        post_subopo(request)

    opo = OPO.objects.get(id=opo)

    context = {
        "opo": opo,
        "form": FormCreateOPORelatorio()
    }

    return render(request, "opo/criar_oporelatorio.html", context)


@login_required
def verifica_opo_vazia(request, id):
    if request.is_ajax:
        opo = OPO.objects.get(id=id)

        if not OPORelatorio.objects.filter(opo=opo).exists():
            OPORelatorio.objects.create(
                opo=opo,
                local=opo.local,
                dataexecucao=opo.datainicio,
                datafinalizacao=opo.datatermino)
    
    return JsonResponse({}, status=200)


@login_required
def atribuir_subopo(request, id):
    try:
        oporelatorio = OPORelatorio.objects.get(id=id)
        paginador = Paginator(
            get_guarnicoes().exclude(
            comandante=request.user.policial.id).filter(
            datafechamento=None), 3)
        numero_pagina = request.GET.get("pagina")
        guarnicoes = paginador.get_page(numero_pagina)

        context = {
            "oporelatorio": oporelatorio,
            "guarnicoes": guarnicoes,
        }

        return render(request, "opo/includes/atribuir_subopo.html", context)
    except Exception:
        pass


@login_required
@csrf_exempt
def atribuir_guarnicao_subopo(request):
    if request.is_ajax and request.method == "POST":
        oporelatorio = OPORelatorio.objects.get(id=request.POST.get("oporelatorio", ""))
        guarnicao = Guarnicao.objects.get(id=request.POST.get("guarnicao", ""))

        if guarnicao.datafechamento is not None:
            return JsonResponse({"message": "Guarnição já encerrada!"}, status=400)
        else:
            oporelatorio.guarnicao_id = guarnicao.id
            oporelatorio.designador_id = request.user.policial.id
            oporelatorio.save()

        return JsonResponse({"message": "Guarnição atribuída com sucesso!"}, status=200)
    else:
        return JsonResponse({}, status=200)


@login_required
def checa_menuopo(request):
    if request.is_ajax and request.method == "GET":
        oporelatorio = OPORelatorio.objects.all()
        opopolicial = OPORelatorio.objects.filter(
            guarnicao=get_guarnicao(request.user.policial.id))

        data = dict()

        if request.user.policial.cargo.cargo == "COORDENADOR DE ÁREA":
            oporelatorio = oporelatorio.filter(opo__designado="coordenadordearea")

            opo = oporelatorio.filter(
                opo__datacriacao__lte=timezone.now(),
                datafinalizacao__gte=timezone.now())

            andamento = oporelatorio.filter(
                designador=request.user.policial.id,
                status="andamento").count()

            data["opo"] = opo.count()
            data["andamento"] = andamento
            data["tipo"] = "coordenadordearea"
        elif request.user.policial.cargo.cargo == "CICOM":
            oporelatorio = oporelatorio.filter(opo__designado="cicom")

            opo = oporelatorio.filter(
                opo__datacriacao__lte=timezone.now(),
                datafinalizacao__gte=timezone.now())

            andamento = oporelatorio.filter(
                designador=request.user.policial.id,
                status="andamento").count()

            data["opo"] = opo.count()
            data["andamento"] = andamento
            data["tipo"] = "cicom"
        elif request.user.policial.companhia.comandante == request.user.policial:
            oporelatorio = oporelatorio.filter(
                opo__designado="comandantecia",
                opo__opocomandantescia__comandante=request.user.policial)

            opo = oporelatorio.filter(
                opo__datacriacao__lte=timezone.now(),
                datafinalizacao__gte=timezone.now())

            andamento = oporelatorio.filter(
                designador=request.user.policial.id,
                status="andamento").count()

            data["opo"] = opo.count()
            data["andamento"] = andamento
            data["tipo"] = "comandantecia"    
        else:
            pendente = opopolicial.filter(
                guarnicao__comandante=request.user.policial.id, status="pendente").count()
            andamento = opopolicial.filter(
                guarnicao__comandante=request.user.policial.id, status="andamento").count()
            data["opo"] = pendente + andamento
            data["tipo"] = "policial"
            data["pendente"] = pendente
            data["andamento"] = andamento

        return JsonResponse(data, status=200)
    
    return JsonResponse({}, status=200)


@login_required
def assumir_opo(request, id):
    if verifica_guarnicao_ativa(request.user.policial.id):
        oporelatorio = OPORelatorio.objects.get(id=id)

        context = {
            "oporelatorio": oporelatorio,
            "form_oporelatorio": FormEditOPORelatorio(instance=oporelatorio),
            "guarnicao_ativa": get_guarnicao(request.user.policial.id)
        }

        return render(request, "opo/assumir_opo.html", context)
    else:
        return redirect("index")


@login_required
@csrf_exempt
def atualiza_opo_relatorio(request, id):
    if request.is_ajax and request.method == "POST":
        instance = OPORelatorio.objects.get(id=id)

        oporelatorio = FormEditOPORelatorio(request.POST, instance=instance)

        data = dict()

        if oporelatorio.is_valid():
            oporelatorio.save()

            data["message"] = "OPO atualizada com sucesso!"

            data["redirect"] = reverse("index")

            return JsonResponse(data, status=200)
        else:
            return JsonResponse(oporelatorio.errors, status=400)


@login_required
def get_subopos(request):
    id = request.GET.get("opo", None)

    oporelatorio = OPORelatorio.objects.filter(
        opo__id=id).order_by("id")

    data = dict()

    if oporelatorio:
        serializer = ListOPORelatorioSerializer(oporelatorio, many=True)
        data["subopos"] = list(serializer.data)

    return JsonResponse(data)


@login_required
def post_subopo(request):
    if request.is_ajax and request.method == "POST":
        oporelatorio = FormCreateOPORelatorio(request.POST or None)

        if oporelatorio.is_valid():
            oporelatorio = oporelatorio.save()

            instance = ListOPORelatorioSerializer(oporelatorio).data
            return JsonResponse({"instance": instance}, status=200)
        else:
            return JsonResponse(oporelatorio.errors, status=400)


@login_required
def edit_subopo(request, id):
    try:
        oporelatorio = OPORelatorio.objects.get(id=id)

        context = {
            "id": oporelatorio.id,
            "oporelatorio": FormCPOEditSubOPO(instance=oporelatorio)
        }

        return render(request, "opo/edits/edit_subopo.html", context)
    except Exception:
        pass


@login_required
def post_edit_subopo(request):
    if request.is_ajax and request.method == "POST":
        instance = OPORelatorio.objects.get(id=request.POST.get("id_subopo"))

        oporelatorio = FormCPOEditSubOPO(request.POST, instance=instance)

        if oporelatorio.is_valid():
            oporelatorio.save()

            return JsonResponse(
                {"message": "SubOPO atualizada."}, status=200)
        else:
            return JsonResponse(oporelatorio.errors, status=400)


@login_required
@csrf_exempt
def delete_subopo(request):
    if request.is_ajax and request.method == "POST":
        data = dict()
        id = request.POST.get("id")
        oporelatorio = OPORelatorio.objects.get(id=id)

        if oporelatorio:
            oporelatorio.delete()
            data["message"] = "SubOPO removida."
        else:
            data["message"] = "Erro!"

        return JsonResponse(data)
