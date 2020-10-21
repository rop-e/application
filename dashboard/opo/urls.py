from django.urls import path
from .opo_views import (
    listar,
    listar_policial,
    adicionar_opo,
    edit_dadosopo,
    post_edit_dadosopo,
    edit_dadossolicitacaoopo,
    post_edit_dadossolicitacaoopo,
    edit_observacaoopo,
    post_edit_observacaoopo,
    post_opo,
    seleciona_comandantescia,
    post_comandantecia,
    get_comandantescia,
    cria_oporelatorio,
    post_subopo,
    post_delete_opo,
    edit_subopo,
    post_edit_subopo,
    delete_subopo,
    get_subopos,
    visualizar_opo,
    visualizar_oporelatorio,
    assumir_opo,
    atualiza_opo_relatorio,
    atribuir_subopo,
    atribuir_guarnicao_subopo,
    checa_menuopo,
    verifica_opo_vazia,
    delete_comandantecia
)

app_name = "opo"

urlpatterns = [
    path(
        "listar/", listar, name="listar"),
    path(
        "listar/policial/",
        listar_policial, name="listar_policial"),
    path(
        "verifica/vazia/<int:id>/",
        verifica_opo_vazia, name="verifica_opo_vazia"),
    path(
        "visualizar/<int:id>/",
        visualizar_opo, name="visualizar_opo"),
    path(
        "visualizar/oporelatorio/<int:id>/",
        visualizar_oporelatorio, name="visualizar_oporelatorio"),
    path(
        "atribuir/subopo/<int:id>/",
        atribuir_subopo, name="atribuir_subopo"),
    path(
        "atribuir/subopo/guarnicao/",
        atribuir_guarnicao_subopo, name="atribuir_guarnicao_subopo"),
    path(
        "adicionar/", adicionar_opo, name="adicionar_opo"),
    path(
        "adicionar/post/", post_opo, name="post_opo"),
    path(
        "adicionar/post/ajax/delete_opo/",
        post_delete_opo, name="post_delete_opo"),
    path(
        "adicionar/selecionar/comandantescia/<int:opo>/",
        seleciona_comandantescia, name="seleciona_comandantescia"),
    path(
        "adicionar/comandantescia/post/ajax",
        post_comandantecia,
        name="post_comandantecia"),
    path(
        "adicionar/comandantescia/post/ajax/delete",
        delete_comandantecia,
        name="delete_comandantecia"),
    path(
        "adicionar/selecionar/comandantescia/get/ajax",
        get_comandantescia,
        name="get_comandantescia"),
    path(
        "adicionar/<int:opo>/oporelatorio/",
        cria_oporelatorio, name="cria_oporelatorio"),
    path(
        "adicionar/subopos/post/ajax/",
        post_subopo,
        name="post_subopo"),
    path(
        "adicionar/subopos/<int:id>/edit",
        edit_subopo, name="edit_subopo"),
    path(
        "adicionar/subopos/edit/post/ajax",
        post_edit_subopo, name="post_edit_subopo"),
    path(
        "adicionar/subopos/get/ajax",
        get_subopos,
        name="get_subopos"),
    path(
        "adicionar/subopos/post/ajax/delete",
        delete_subopo,
        name="delete_subopo"),
    path(
        "edit/dados/<int:id>/",
        edit_dadosopo, name="edit_dadosopo"),
    path(
        "edit/dados/post/ajax",
        post_edit_dadosopo, name="post_edit_dadosopo"),
    path(
        "edit/solicitacao/<int:id>/",
        edit_dadossolicitacaoopo, name="edit_dadossolicitacaoopo"),
    path(
        "edit/solicitacao/post/ajax",
        post_edit_dadossolicitacaoopo, name="post_edit_dadossolicitacaoopo"),
    path(
        "edit/observacao/<int:id>/",
        edit_observacaoopo, name="edit_observacaoopo"),
    path(
        "edit/observacao/post/ajax",
        post_edit_observacaoopo, name="post_edit_observacaoopo"),
    path(
        "checa/menu/get/ajax/",
        checa_menuopo, name="checa_menuopo"),
    path(
        "policial/<int:id>/assumir/",
        assumir_opo,
        name="assumir_opo"),
    path(
        "policial/atualizar/<int:id>/",
        atualiza_opo_relatorio,
        name="atualiza_opo_relatorio")
]
