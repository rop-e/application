from django.urls import path
from .policial_views import (
    buscar_policial,
    atualizar_senha,
    atualizar_foto,
    atualizar_email,
    perfil,
    listar_policiais,
    mostrar,
    registrar,
    remover
)

app_name = "policial"

urlpatterns = [
    path(
        "",
        perfil,
        name="perfil"),
    path(
        "policial/ajax/post/atualizar_senha/",
        atualizar_senha,
        name="atualizar_senha"),
    path(
        "policial/ajax/post/atualizar_foto/",
        atualizar_foto,
        name="atualizar_foto"),
    path(
        "policial/ajax/post/atualizar_email/",
        atualizar_email,
        name="atualizar_email"),
    path(
        "policiais/",
        listar_policiais,
        name="listar_policiais"),
    path(
        "policiais/registrar/",
        registrar,
        name="registrar"),
    path(
        "policiais/mostrar/<int:id>/",
        mostrar,
        name="mostrar"),
    path(
        "policiais/remover/<int:id>/",
        remover,
        name="remover"),
    path(
        "ajax/get/buscar/guarnicao/<int:guarnicao>/",
        buscar_policial, name="buscar_policial")
]
