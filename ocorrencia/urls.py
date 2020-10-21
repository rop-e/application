from django.urls import path
from .views import (
    OcorrenciaListCreateView,
    OcorrenciaDetailsUpdateDeleteView,
    TipoInfracaoListCreateView,
    TipoOcorrenciaListCreateView
)

urlpatterns = [
    path(
        '',
        OcorrenciaListCreateView.as_view(),
        name='create'),
    path(
        '<int:pk>/',
        OcorrenciaDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        'tipoinfracao/',
        TipoInfracaoListCreateView.as_view(),
        name='create'),
    path(
        'tipoocorrencia/',
        TipoOcorrenciaListCreateView.as_view(),
        name='create'),
]
