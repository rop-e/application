from django.urls import path
from .guarnicao_views import (
    listar_guarnicoes_comandante,
    visualizar_guarnicao,
    adicionar_guarnicao,
    post_guarnicao,
    post_delete_guarnicao,
    get_ocorrencias_guarnicao,
    get_rats_guarnicao,
    encerrar_guarnicao,
    post_encerra_guarnicao,
    get_viaturas,
    listar_companhias,
    remover_companhia,
    adicionar_companhia,
    adicionar_policial_guarnicao,
    post_policial,
    get_policiais_guarnicao,
    delete_policial,
    get_aits_guarnicao,
    get_rrds_guarnicao,
    get_travs_guarnicao,
    post_ait,
    edit_ait,
    post_edit_ait,
    delete_ait,
    post_rrd,
    edit_rrd,
    post_edit_rrd,
    delete_rrd,
    post_trav,
    edit_trav,
    post_edit_trav,
    delete_trav,
    listar_guarnicoes_ativas,
    verifica_andamento,
    ajax_guarnicoes_ativas,
    ajax_verifica_guarnicao_ativa,
    geraemostrapdfguarnicao,



    verifica_guarnicao_bloqueada,
    bloqueia_guarnicao,
    listar_guarnicoes_todas,
    permutar
)

app_name = "guarnicao"

urlpatterns = [
    path(
        "verifica/bloqueada/",
        verifica_guarnicao_bloqueada,
        name="verifica_guarnicao_bloqueada"),
    path(
        "altera/bloqueia/",
        bloqueia_guarnicao,
        name="bloqueia_guarnicao"),
    path(
        "todas/",
        listar_guarnicoes_todas,
        name="listar_guarnicoes_todas"),
    path(
        "permutar/",
        permutar,
        name="permutar"),
    path(
        "comandante/",
        listar_guarnicoes_comandante,
        name="listar_guarnicoes_comandante"),
    path(
        "ativas/",
        listar_guarnicoes_ativas,
        name="listar_guarnicoes_ativas"),
    path(
        "visualizar/<int:id>/",
        visualizar_guarnicao,
        name="visualizar_guarnicao"),
    path(
        "visualizar/<int:id>/pdf/", geraemostrapdfguarnicao, name="geraemostrapdfguarnicao"),
    path(
        "post/ajax/adicionar/",
        post_guarnicao,
        name="post_guarnicao"),
    path(
        "adicionar/",
        adicionar_guarnicao,
        name="adicionar_guarnicao"),
    path(
        "post/ajax/delete_guarnicao/",
        post_delete_guarnicao,
        name="post_delete_guarnicao"),
    path(
        "<int:guarnicao>/encerrar/",
        encerrar_guarnicao,
        name="encerrar_guarnicao"),
    path(
        "post/ajax/encerra",
        post_encerra_guarnicao,
        name="post_encerra_guarnicao"),
    path(
        "get/ajax/ocorrencias",
        get_ocorrencias_guarnicao,
        name="get_ocorrencias_guarnicao"),
    path(
        "get/ajax/rats",
        get_rats_guarnicao,
        name="get_rats_guarnicao"),
    path(
        "get/ajax/aits",
        get_aits_guarnicao,
        name="get_aits_guarnicao"),
    path(
        "get/ajax/rrds",
        get_rrds_guarnicao,
        name="get_rrds_guarnicao"),
    path(
        "get/ajax/travs",
        get_travs_guarnicao,
        name="get_travs_guarnicao"),
    path(
        "post/ajax/ait",
        post_ait,
        name="post_ait"),
    path(
        "ait/<int:id>/edit",
        edit_ait,
        name="edit_ait"),
    path(
        "post/ajax/ait/edit",
        post_edit_ait,
        name="post_edit_ait"),
    path(
        "post/ajax/ait/delete",
        delete_ait,
        name="delete_ait"),
    path(
        "post/ajax/rrd",
        post_rrd,
        name="post_rrd"),
    path(
        "rrd/<int:id>/edit",
        edit_rrd,
        name="edit_rrd"),
    path(
        "post/ajax/rrd/edit",
        post_edit_rrd,
        name="post_edit_rrd"),
    path(
        "post/ajax/rrd/delete",
        delete_rrd,
        name="delete_rrd"),
    path(
        "post/ajax/trav",
        post_trav,
        name="post_trav"),
    path(
        "trav/<int:id>/edit",
        edit_trav,
        name="edit_trav"),
    path(
        "post/ajax/trav/edit",
        post_edit_trav,
        name="post_edit_trav"),
    path(
        "post/ajax/trav/delete",
        delete_trav,
        name="delete_trav"),
    path(
        "get/ajax/viaturas",
        get_viaturas,
        name="get_viaturas"),
    path(
        "<int:guarnicao>/adicionar/policial/",
        adicionar_policial_guarnicao,
        name="adicionar_policial_guarnicao"),
    path(
        "post/ajax/policial",
        post_policial,
        name="post_policial"),
    path(
        "policiais/get/ajax",
        get_policiais_guarnicao,
        name="get_policiais_guarnicao"),
    path(
        "post/ajax/policial/delete",
        delete_policial,
        name="delete_policial"),
    path(
        "companhia/",
        listar_companhias,
        name="listar_companhias"),
    path(
        "companhia/adicionar/",
        adicionar_companhia,
        name="adicionar_companhia"),
    path(
        "companhia/remover/<int:id>/",
        remover_companhia,
        name="remover_companhia"),
    path(
        "verifica/ocorrencias/andamento/",
        verifica_andamento,
        name="verifica_andamento"),
    path(
        "get/ativas/",
        ajax_guarnicoes_ativas,
        name="ajax_guarnicoes_ativas"),
    path(
        "ativa/verifica/",
        ajax_verifica_guarnicao_ativa,
        name="ajax_verifica_guarnicao_ativa")
]