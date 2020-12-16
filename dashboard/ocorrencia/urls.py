from django.urls import path
from .ocorrencia_views import (
    listar,
    mostrar,
    checa_policial_guarnicao,
    adicionar_ocorrencia,
    post_ocorrencia,
    adicionar_acessorios,
    post_preview_ocorrencia,
    preview_ocorrencia,
    edit_relatorio,
    post_edit_relatorio,
    get_apreensoes,
    post_delete_ocorrencia,
    finalizar_ocorrencia,
    get_aditamentos,
    post_aditamento,
    cancel_aditamento,
    verifica_ocorrencia_nao_finalizada,
    listar_ocorrencias_sem_finalizar,
    post_anexo,
    get_anexos,
    delete_anexo,
    geraemostrapdfocorrencia,
    vincular_ocorrencia,
    post_vincular_ocorrencia
)

app_name = "ocorrencia"

urlpatterns = [
    path(
        "listar/", listar, name="listar"),
    path(
        "listar/pendentes/",
        listar_ocorrencias_sem_finalizar,
        name="listar_ocorrencias_sem_finalizar"),
    path(
        "mostrar/<int:id>/", mostrar, name="mostrar"),
    path(
        "mostrar/<int:id>/pdf/", geraemostrapdfocorrencia, name="geraemostrapdfocorrencia"),
    path(
        "post/ajax/checar_policial_guarnicao/",
        checa_policial_guarnicao, name="checa_policial_guarnicao"),
    path(
        "adicionar/", adicionar_ocorrencia, name="adicionar_ocorrencia"),
    path(
        "adicionar/ocorrencia/", post_ocorrencia, name="post_ocorrencia"),
    path(
        "adicionar/ocorrencia/<int:ocorrencia>/acessorios/",
        adicionar_acessorios, name="adicionar_acessorios"),
    path(
        "get/ajax/anexos",
        get_anexos,
        name="get_anexos"),
    path(
        "post/ajax/anexo",
        post_anexo,
        name="post_anexo"),
    path(
        "post/ajax/anexo/delete",
        delete_anexo,
        name="delete_anexo"),
    path(
        "adicionar/ocorrencia/<int:id>/vincular/",
        vincular_ocorrencia, name="vincular_ocorrencia"),
    path(
        "adicionar/ocorrencia/vincular/post/",
        post_vincular_ocorrencia, name="post_vincular_ocorrencia"),
    path(
        "adicionar/ocorrencia/preview/",
        post_preview_ocorrencia, name="post_preview_ocorrencia"),
    path(
        "ocorrencia/preview/relatorio/<int:id>/edit",
        edit_relatorio, name="edit_relatorio"),
    path(
        "ocorrencia/preview/relatorio/post/ajax",
        post_edit_relatorio, name="post_edit_relatorio"),
    path(
        "adicionar/ocorrencia/<int:id>/preview/",
        preview_ocorrencia, name="preview_ocorrencia"),
    path(
        "ocorrencia/preview/get/apreensoes",
        get_apreensoes, name="get_apreensoes"),
    path(
        "ocorrencia/post/ajax/delete_ocorrencia/",
        post_delete_ocorrencia, name="post_delete_ocorrencia"),
    path(
        "ocorrencia/finaliza/",
        finalizar_ocorrencia, name="finalizar_ocorrencia"),
    path(
        "ocorrencia/get/ajax/aditamento/",
        get_aditamentos, name="get_aditamentos"),
    path(
        "ocorrencia/post/ajax/aditamento",
        post_aditamento, name="post_aditamento"),
    path(
        "ocorrencia/post/ajax/aditamento/cancel",
        cancel_aditamento, name="cancel_aditamento"),
    path(
        "ocorrencia/verifica/pendente/get/ajax/",
        verifica_ocorrencia_nao_finalizada,
        name="verifica_ocorrencia_nao_finalizada")
]
