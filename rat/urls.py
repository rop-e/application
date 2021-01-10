from django.urls import path
from .views import (
    TipoAcidenteListCreateView,
    TipoAcidenteDetailsUpdateDeleteView,
    CondicaoViaListCreateView,
    CondicaoViaDetailsUpdateDeleteView,
    CondicaoSinalizacaoListCreateView,
    CondicaoSinalizacaoDetailsUpdateDeleteView,
    TracadoViaListCreateView,
    TracadoViaDetailsUpdateDeleteView,
    CondicaoMeteorologicaListCreateView,
    CondicaoMeteorologicaDetailsUpdateDeleteView,
    PavimentacaoListCreateView,
    PavimentacaoDetailsUpdateDeleteView,
    RATListCreateView,
    RATDetailsUpdateDeleteView,
    RATObjetosListCreateView,
    RATObjetosDetailsUpdateDeleteView,
    RATVeiculosListCreateView,
    RATVeiculosDetailsUpdateDeleteView,
    RATVeiculoEnvolvidosListCreateView,
    RATVeiculoEnvolvidosDetailsUpdateDeleteView,
    RATsGuarnicaoListView,
    ApreensoesRATListView
)

urlpatterns = [
    path(
        "guarnicao/<int:id>/",
        RATsGuarnicaoListView.as_view(),
        name="rats_guarnicao"),
    path(
        "tipoacidente/",
        TipoAcidenteListCreateView.as_view(),
        name="create"),
    path(
        "tipoacidente/<int:pk>/",
        TipoAcidenteDetailsUpdateDeleteView.as_view(),
        name="detalhe"),
    path(
        "condicaovia/",
        CondicaoViaListCreateView.as_view(),
        name="create"),
    path(
        "condicaovia/<int:pk>/",
        CondicaoViaDetailsUpdateDeleteView.as_view(),
        name="detalhe"),
    path(
        "condicaosinalizacao/",
        CondicaoSinalizacaoListCreateView.as_view(),
        name="create"),
    path(
        "condicaosinalizacao/<int:pk>/",
        CondicaoSinalizacaoDetailsUpdateDeleteView.as_view(),
        name="detalhe"),
    path(
        "tracadovia/",
        TracadoViaListCreateView.as_view(),
        name="create"),
    path(
        "tracadovia/<int:pk>/",
        TracadoViaDetailsUpdateDeleteView.as_view(),
        name="detalhe"),
    path(
        "condicaometeorologica/",
        CondicaoMeteorologicaListCreateView.as_view(),
        name="create"),
    path(
        "condicaometeorologica/<int:pk>/",
        CondicaoMeteorologicaDetailsUpdateDeleteView.as_view(),
        name="detalhe"),
    path(
        "pavimentacao/",
        PavimentacaoListCreateView.as_view(),
        name="create"),
    path(
        "pavimentacao/<int:pk>/",
        PavimentacaoDetailsUpdateDeleteView.as_view(),
        name="detalhe"),
    path(
        "",
        RATListCreateView.as_view(),
        name="create"),
    path(
        "<int:pk>/",
        RATDetailsUpdateDeleteView.as_view(),
        name="detalhe"),
    path(
        "apreensoes/<int:pk>/",
        ApreensoesRATListView.as_view(),
        name="apreensoes"),
    path(
        "objetos/",
        RATObjetosListCreateView.as_view(),
        name="create"),
    path(
        "objetos/<int:pk>/",
        RATObjetosDetailsUpdateDeleteView.as_view(),
        name="detalhe"),
    path(
        "veiculos/",
        RATVeiculosListCreateView.as_view(),
        name="create"),
    path(
        "veiculos/<int:pk>/",
        RATVeiculosDetailsUpdateDeleteView.as_view(),
        name="detalhe"),
    path(
        "veiculoenvolvidos/",
        RATVeiculoEnvolvidosListCreateView.as_view(),
        name="create"),
    path(
        "veiculoenvolvidos/<int:pk>/",
        RATVeiculoEnvolvidosDetailsUpdateDeleteView.as_view(),
        name="detalhe")
]
