from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import (
    TipoServico,
    ModalidadedePoliciamento,
    Companhia,
    Guarnicao,
    GuarnicaoAIT,
    GuarnicaoRRD,
    GuarnicaoTRAV,
    Permuta
)
from endereco.models import Municipios

admin.site.register(TipoServico)
admin.site.register(ModalidadedePoliciamento)
admin.site.register(GuarnicaoAIT)
admin.site.register(GuarnicaoRRD)
admin.site.register(GuarnicaoTRAV)
admin.site.register(Permuta)


class FinalizadasListFilter(admin.SimpleListFilter):
    title = 'Finalizadas'
    parameter_name = 'finalizada'

    def lookups(self, request, model_admin):
        return (
            ('sim', 'Sim'),
            ('nao',  'Não'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'sim':
            return queryset.filter(datafechamento__isnull=False)
        if self.value() == 'nao':
            return queryset.filter(datafechamento__isnull=True)

        return queryset


class GuarnicaoAdmin(admin.ModelAdmin):
    list_display = (
        "comandante",
        "municipio",
        "dataabertura",
        "datafechamento",
        "ativo"
    )
    search_fields = ["comandante__nomeguerra"]
    list_filter = [FinalizadasListFilter, "ativo", ('municipio', RelatedOnlyFieldListFilter)]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "municipio":
            kwargs["queryset"] = Municipios.objects.filter(
                batalhaomunicipios__batalhao=request.user.policial.batalhao)\
                    .order_by("batalhaomunicipios__municipio__nome")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CompanhiaAdmin(admin.ModelAdmin):
    list_display = (
        "companhia",
        "comandante"
    )


admin.site.register(Guarnicao, GuarnicaoAdmin)
admin.site.register(Companhia, CompanhiaAdmin)
