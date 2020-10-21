from django.contrib import admin
from .models import (
        LocalRecebedor,
        AgenteRecebedor
    )

admin.site.register(LocalRecebedor)
admin.site.register(AgenteRecebedor)
