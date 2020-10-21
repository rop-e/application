from django.contrib import admin
from .models import (
    Batalhao,
    BatalhaoMunicipios
)

admin.site.register(Batalhao)
admin.site.register(BatalhaoMunicipios)
