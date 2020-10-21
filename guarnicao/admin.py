from django.contrib import admin
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


class GuarnicaoAdmin(admin.ModelAdmin):
    list_display = (
        "comandante",
        "municipio",
        "dataabertura",
        "datafechamento"
    )

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
