from django.contrib import admin
from .models import (
    Estados,
    Municipios,
    Endereco
)

admin.site.register(Estados)


class MunicipiosAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_uf',
        'nome',
    )
    list_filter = ('codigo_uf__nome',)
    filter_horizontal = ()
    ordering = ('nome',)


admin.site.register(Municipios, MunicipiosAdmin)


class EnderecoAdmin(admin.ModelAdmin):
    fields = (
        'municipio',
        'numero',
        'rua',
        'bairro',
        'complemento',
        'observacao',
        'latitude',
        'longitude'
    )
    list_display = (
        'rua',
        'numero',
        'bairro',
        'municipio'
    )


admin.site.register(Endereco, EnderecoAdmin)
