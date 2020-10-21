from django.urls import path
from .envolvido_views import (
    get_envolvidos,
    get_envolvidosrat,
    post_envolvidoocorrencia,
    post_envolvidorat,
    checar_nome_existente,
    edit_envolvido_ocorrencia,
    post_edit_envolvidoocorrencia,
    edit_envolvido_rat,
    post_edit_envolvidorat,
    delete_envolvido
)

app_name = "envolvido"

urlpatterns = [
    path(
        "get/ajax/envolvidos",
        get_envolvidos,
        name="get_envolvidos"),

    path(
        "rat/get/ajax/envolvidos",
        get_envolvidosrat,
        name="get_envolvidosrat"),
    path(
        "ocorrencia/post/ajax/envolvido",
        post_envolvidoocorrencia,
        name="post_envolvidoocorrencia"),
    path(
        "rat/post/ajax/envolvido",
        post_envolvidorat,
        name="post_envolvidorat"),
    path(
        "get/ajax/validar/nome",
        checar_nome_existente,
        name="checar_nome_existente"),
    path(
        "envolvido/ocorrencia/<int:id>/edit",
        edit_envolvido_ocorrencia,
        name="edit_envolvido_ocorrencia"),
    path(
        "envolvido/ocorrencia/post/ajax",
        post_edit_envolvidoocorrencia,
        name="post_edit_envolvidoocorrencia"),
    path(
        "envolvido/rat/<int:id>/edit",
        edit_envolvido_rat,
        name="edit_envolvido_rat"),
    path(
        "envolvido/rat/post/ajax",
        post_edit_envolvidorat,
        name="post_edit_envolvidorat"),
    path(
        "post/ajax/envolvido/delete",
        delete_envolvido,
        name="delete_envolvido")
]
