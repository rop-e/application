from django.contrib import admin
from .models import (
    TipoEnvolvimento,
    Envolvido,
    Lesao
)


class TipoEnvolvimentoAdmin(admin.ModelAdmin):
    list_display = (
        'tipo',
        'rat',
    )


admin.site.register(TipoEnvolvimento, TipoEnvolvimentoAdmin)
admin.site.register(Envolvido)
admin.site.register(Lesao)
