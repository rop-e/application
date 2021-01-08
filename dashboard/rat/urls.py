from django.urls import path
from .rat_views import (
    listar,
    mostrar,
    edit_rat,
    verifica_rat_nao_finalizada,
    listar_rats_sem_finalizar,
    checa_policial_guarnicao,
    adicionar_rat,
    post_rat,
    post_edit_rat,
    adicionar_veiculos_envolvidos,
    post_delete_rat,
    post_anexo,
    get_anexos,
    delete_anexo,
    get_objetos,
    post_objeto,
    edit_objeto,
    post_edit_objeto,
    delete_objeto,
    edit_relatorio,
    post_edit_relatorio,
    get_veiculos,
    post_veiculo,
    checar_veiculo_placa_existente,
    checar_veiculo_chassi_existente,
    edit_veiculo,
    post_edit_veiculo,
    delete_veiculo,
    post_preview_rat,
    preview_rat,
    geraemostrapdfrat
)

app_name = "rat"

urlpatterns = [
    path(
        "listar/", listar, name="listar"),
    path(
        "mostrar/<int:id>/", mostrar, name="mostrar"),
    path(
        "mostrar/<int:id>/pdf/", geraemostrapdfrat, name="geraemostrapdfrat"),
    path(
        "rat/<int:id>/edit",
        edit_rat,
        name="edit_rat"),
    path(
        "rat/post/ajax/",
        post_edit_rat,
        name="post_edit_rat"),
    path(
        "relatorio/<int:id>/edit",
        edit_relatorio, name="edit_relatorio"),
    path(
        "relatorio/post/ajax",
        post_edit_relatorio, name="post_edit_relatorio"),
    path(
        "verifica/pendente/get/ajax/",
        verifica_rat_nao_finalizada,
        name="verifica_rat_nao_finalizada"),
    path(
        "listar/pendentes/",
        listar_rats_sem_finalizar,
        name="listar_rats_sem_finalizar"),
    path(
        "post/ajax/checar_policial_guarnicao/",
        checa_policial_guarnicao, name="checa_policial_guarnicao"),
    path(
        "adicionar/", adicionar_rat, name="adicionar_rat"),
    path(
        "adicionar/rat/", post_rat, name="post_rat"),
    path(
        "adicionar/rat/<int:rat>/veiculos_envolvidos/",
        adicionar_veiculos_envolvidos, name="adicionar_veiculos_envolvidos"),
    path(
        "adicionar/rat/preview/",
        post_preview_rat, name="post_preview_rat"),
    path(
        "adicionar/rat/<int:id>/preview/",
        preview_rat, name="preview_rat"),
    path(
        "rat/post/ajax/delete_rat/",
        post_delete_rat, name="post_delete_rat"),
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
        "get/ajax/objetos",
        get_objetos,
        name="get_objetos"),
    path(
        "post/ajax/objeto",
        post_objeto,
        name="post_objeto"),
    path(
        "objeto/<int:id>/edit",
        edit_objeto,
        name="edit_objeto"),
    path(
        "objeto/post/ajax/",
        post_edit_objeto,
        name="post_edit_objeto"),
    path(
        "post/ajax/objeto/delete",
        delete_objeto,
        name="delete_objeto"),
    path(
        "get/ajax/veiculos",
        get_veiculos,
        name="get_veiculos"),
    path(
        "post/ajax/veiculo",
        post_veiculo,
        name="post_veiculo"),
    path(
        "get/ajax/validar/veiculo/placa",
        checar_veiculo_placa_existente,
        name="checar_veiculo_placa_existente"),
    path(
        "get/ajax/validar/veiculo/chassi",
        checar_veiculo_chassi_existente,
        name="checar_veiculo_chassi_existente"),
    path(
        "veiculo/<int:id>/edit",
        edit_veiculo,
        name="edit_veiculo"),
    path(
        "veiculo/post/ajax",
        post_edit_veiculo,
        name="post_edit_veiculo"),
    path(
        "post/ajax/veiculo/delete",
        delete_veiculo,
        name="delete_veiculo")
]
