from django.contrib import admin
from .models import (
    TipoAcidente,
    CondicaoVia,
    CondicaoSinalizacao,
    TracadoVia,
    CondicaoMeteorologica,
    Pavimentacao,
    RAT,
    RATObjetos,
    RATVeiculos,
    RATVeiculoEnvolvidos
)


admin.site.register(TipoAcidente)
admin.site.register(CondicaoVia)
admin.site.register(CondicaoSinalizacao)
admin.site.register(TracadoVia)
admin.site.register(CondicaoMeteorologica)
admin.site.register(Pavimentacao)
admin.site.register(RAT)
admin.site.register(RATObjetos)
admin.site.register(RATVeiculos)


class RATVeiculoEnvolvidosAdmin(admin.ModelAdmin):
    model = RATVeiculoEnvolvidos

    list_display = (
        'ratveiculos',
        'envolvido',
        'get_tipoenvolvimento'
    )

    def get_tipoenvolvimento(self, obj):
        return obj.envolvido.tipoenvolvimento

    get_tipoenvolvimento.short_description = 'Tipo de envolvimento'


admin.site.register(RATVeiculoEnvolvidos, RATVeiculoEnvolvidosAdmin)
