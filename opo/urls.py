from django.urls import path
from .views import (
    OPOTipoEventoListCreateView,
    OPOTipoEventoDetailsUpdateDeleteView,
    OPOListCreateView,
    OPODetailsUpdateDeleteView,
    OPORelatorioListCreateView,
    OPORelatorioDetailsUpdateDeleteView
)

urlpatterns = [
    path(
        'tipoevento/',
        OPOTipoEventoListCreateView.as_view(),
        name='create'),
    path(
        'tipoevento/<int:pk>/',
        OPOTipoEventoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        '',
        OPOListCreateView.as_view(),
        name='create'),
    path(
        '<int:pk>/',
        OPODetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        'relatorio/',
        OPORelatorioListCreateView.as_view(),
        name='create'),
    path(
        'relatorio/<int:pk>/',
        OPORelatorioDetailsUpdateDeleteView.as_view(),
        name='detalhe')
]
