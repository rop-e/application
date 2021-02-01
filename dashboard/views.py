from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ocorrencia.models import (
    Ocorrencia,
    Infracao
)
from django.utils import timezone
from django.db.models import Count


@login_required
def dashboard(request):
    ocorrencias = Ocorrencia.objects.filter(
        dataocorrencia__date__gte=timezone.localdate(timezone.now())).count()

    infracao = Infracao.objects.filter(
        ocorrencia__isnull=False,
        ocorrencia__dataocorrencia__date__gte=timezone.localdate(timezone.now())).distinct()

    ocorrencias_infracao = infracao.values('tipo').annotate(Count('tipo'))

    context = {
        "ocorrencias": ocorrencias,
        "infracoes": infracao,
        "ocorrencias_infracao": ocorrencias_infracao
    }

    return render(request, "painel.html", context)
