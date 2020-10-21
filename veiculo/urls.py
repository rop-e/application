from django.urls import path
from .views import (
    CategoriaVeiculoListCreateView,
    CategoriaVeiculoDetailsUpdateDeleteView,
    MarcaVeiculoListCreateView,
    MarcaVeiculoDetailsUpdateDeleteView,
    VeiculoListCreateView,
    VeiculoDetailsUpdateDeleteView
)

urlpatterns = [
    path(
        'categoria/',
        CategoriaVeiculoListCreateView.as_view(),
        name='create'),
    path(
        'categoria/<int:pk>/',
        CategoriaVeiculoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),

    path(
        'marca/',
        MarcaVeiculoListCreateView.as_view(),
        name='create'),
    path(
        'marca/<int:pk>/',
        MarcaVeiculoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),

    path(
        '',
        VeiculoListCreateView.as_view(),
        name='create'),
    path(
        '<int:pk>/',
        VeiculoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
]
