from django.contrib import admin
from .models import (
        Procedimento,
        ProcedimentoOcorrencia
    )

admin.site.register(Procedimento)


class ProcedimentoOcorrenciaAdmin(admin.ModelAdmin):
    fields = (
        'procedimento',
        'ocorrencia',
        'observacao',
    )
    list_display = (
       'procedimento',
    )


admin.site.register(ProcedimentoOcorrencia, ProcedimentoOcorrenciaAdmin)
