from django.contrib import admin
from .models import (
    Funcao,
    PolicialViatura
)

admin.site.register(Funcao)


class PolicialViaturaAdmin(admin.ModelAdmin):
    fields = (
        'guarnicao',
        'policial',
        'funcao',
        'viatura',
        'condicaoviatura',
        'ativo',
        'kmsaida',
        'kmvolta'
    )
    list_display = (
        'policial',
        'list_guarnicao',
        'funcao',
        'viatura'
    )

    def list_guarnicao(self, obj):
        return '({}) - {}({})'.format(
            obj.guarnicao.pk,
            obj.guarnicao,
            obj.guarnicao.dataabertura.strftime('%d/%m/%Y - %H:%M'))
    
    list_guarnicao.short_description = "Guarnição"


admin.site.register(PolicialViatura, PolicialViaturaAdmin)
