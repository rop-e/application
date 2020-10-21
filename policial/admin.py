from django.contrib import admin
from .models import (
    PostoGraduacao,
    Cargo,
    TipoSanguineo,
    Policial
)


admin.site.register(PostoGraduacao)
admin.site.register(Cargo)
admin.site.register(TipoSanguineo)


class PolicialAdmin(admin.ModelAdmin):
    model = Policial

    list_display = (
        'matricula',
        'get_nome',
        'companhia',
        'cargo'
    )
    list_filter = (
        'postograduacao',
        'matricula__sexo',
        'companhia',
        'cargo'
    )
    fields = (
        'matricula',
        'foto',
        'batalhao',
        'postograduacao',
        'companhia',
        'cargo',
        'tiposanguineo',
        'nomeguerra',
        'dtpraca',
    )
    search_fields = (
        'matricula__matricula',
        'matricula__nome'
    )
    ordering = ('matricula__nome',)

    def get_nome(self, obj):
        return obj.matricula.nome

    get_nome.short_description = 'Nome'


admin.site.register(Policial, PolicialAdmin)
