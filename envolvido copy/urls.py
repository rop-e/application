from django.urls import path
from .views import (
    TipoEnvolvimentoListCreateView,
    TipoEnvolvimentoDetailsUpdateDeleteView,
    EnvolvidoListCreateView,
    EnvolvidoDetailsUpdateDeleteView,
    TipoLesaoListCreateView,
    TipoLesaoDetailsUpdateDeleteView,
    LesaoListCreateView,
    LesaoDetailsUpdateDeleteView
)

urlpatterns = [
    path(
        'tipoenvolvimento/',
        TipoEnvolvimentoListCreateView.as_view(),
        name='create'),
    path(
        'tipoenvolvimento/<int:pk>/',
        TipoEnvolvimentoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        '',
        EnvolvidoListCreateView.as_view(),
        name='create'),
    path(
        '<int:pk>/',
        EnvolvidoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        'tipolesao/',
        TipoLesaoListCreateView.as_view(),
        name='create'),
    path(
        'tipolesao/<int:pk>/',
        TipoLesaoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        'lesao/',
        LesaoListCreateView.as_view(),
        name='create'),
    path(
        'lesao/<int:pk>/',
        LesaoDetailsUpdateDeleteView.as_view(),
        name='detalhe')
]
