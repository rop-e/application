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
        dataocorrencia__date__gte=timezone.now().date())

    infracao = Infracao.objects.filter(
        ocorrencia__isnull=False,
        ocorrencia__dataocorrencia__date__gte=timezone.now().date()).distinct()

    context = {
        "ocorrencias": ocorrencias,
        "infracoes": infracao
    }

    return render(request, "painel.html", context)
