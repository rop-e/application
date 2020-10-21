from django.contrib import admin
from .models import (
    AcessoriosOcorrencia,
    MunicaoAcessorio,
    VeiculoAcessorio,
    TipoDoc,
    DocAcessorio,
    TiposDiversos,
    DiversosAcessorio,
    FabricanteArma,
    TipoArma,
    Arma,
    ArmaAcessorio,
    TipoDroga,
    ArmazenamentoDroga,
    DrogaAcessorio,
    Calibre,
    UnidadeMedida
)

admin.site.register(AcessoriosOcorrencia)
admin.site.register(Calibre)
admin.site.register(MunicaoAcessorio)
admin.site.register(VeiculoAcessorio)
admin.site.register(TipoDoc)
admin.site.register(DocAcessorio)
admin.site.register(TiposDiversos)
admin.site.register(DiversosAcessorio)
admin.site.register(FabricanteArma)
admin.site.register(TipoArma)
admin.site.register(Arma)
admin.site.register(ArmaAcessorio)
admin.site.register(TipoDroga)
admin.site.register(ArmazenamentoDroga)
admin.site.register(DrogaAcessorio)
admin.site.register(UnidadeMedida)
