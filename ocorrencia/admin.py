from django.contrib import admin
from .models import (
    TipoOcorrencia,
    Infracao,
    Ocorrencia,
    GuarnicaoApoio,
    ObservacaoOcorrencia
)

admin.site.register(TipoOcorrencia)
admin.site.register(Infracao)
admin.site.register(Ocorrencia)
admin.site.register(GuarnicaoApoio)
admin.site.register(ObservacaoOcorrencia)
