from django.contrib import admin
from .models import (
    CategoriaVeiculo,
    MarcaVeiculo,
    Veiculo
)

admin.site.register(CategoriaVeiculo)
admin.site.register(MarcaVeiculo)
admin.site.register(Veiculo)
