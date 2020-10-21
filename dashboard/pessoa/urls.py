from django.urls import path
from .pessoa_views import buscar_pessoa

app_name = "pessoa"

urlpatterns = [
    path(
        "ajax/get/buscar/", buscar_pessoa, name="buscar_pessoa"),
]
