from django.contrib import admin
from .models import (
    OPO,
    OPORelatorio,
    OPOTipoEvento,
    OPOComandantesCIA
)
from policial.models import Policial

class OPOAdmin(admin.ModelAdmin):
    list_display = (
        'numeroopo',
        'titulo',
        'opotipoevento',
        'local',
        'datasolicitacao'
    )


class OPORelatorioAdmin(admin.ModelAdmin):
    list_display = (
        'opo',
        'local',
        'status',
        'guarnicao',
        'relatorio'
    )


admin.site.register(OPO, OPOAdmin)
admin.site.register(OPORelatorio, OPORelatorioAdmin)
admin.site.register(OPOTipoEvento)
admin.site.register(OPOComandantesCIA)
