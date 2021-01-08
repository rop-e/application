from django.contrib import admin
from .models import (
    Funcao,
    PolicialViatura
)

admin.site.register(Funcao)


class FinalizadasListFilter(admin.SimpleListFilter):
    title = 'Guarnições Finalizadas'
    parameter_name = 'guarnicao_finalizada'

    def lookups(self, request, model_admin):
        return (
            ('sim', 'Sim'),
            ('nao',  'Não'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'sim':
            return queryset.filter(guarnicao__datafechamento__isnull=False)
        if self.value() == 'nao':
            return queryset.filter(guarnicao__datafechamento__isnull=True)

        return queryset


class PolicialViaturaAdmin(admin.ModelAdmin):
    list_filter = ["ativo", FinalizadasListFilter]
    list_display = (
        "policial",
        "list_guarnicao",
        "funcao",
        "viatura",
        "ativo",
        "guarnicao_finalizada"
    )

    def list_guarnicao(self, obj):
        return "({}) - {}({})".format(
            obj.guarnicao.pk,
            obj.guarnicao,
            obj.guarnicao.dataabertura.strftime("%d/%m/%Y - %H:%M"))

    def guarnicao_finalizada(self, obj):
        return True if obj.guarnicao.datafechamento else False
    
    guarnicao_finalizada.short_description = "Guarnição Finalizada"
    guarnicao_finalizada.boolean = True
    
    list_guarnicao.short_description = "Guarnição"


admin.site.register(PolicialViatura, PolicialViaturaAdmin)
