from django.urls import path
from .views import (
    OcorrenciaListCreateView,
    OcorrenciaDetailsUpdateDeleteView,
    TipoInfracaoListCreateView,
    TipoOcorrenciaListCreateView,
    OcorrenciaDateFilterListView,
    OcorrenciaEnvolvidosFilterListView
)

urlpatterns = [
    path(
        '',
        OcorrenciaListCreateView.as_view(),
        name='create'),
    path(
        'datefilter/<int:diaI>/<int:mesI>/<int:anoI>/<int:diaF>/<int:mesF>/<int:anoF>/',
        OcorrenciaDateFilterListView.as_view(),
        name='datefilter'),
    path(
        'envolvido/<str:envolvido>/',
        OcorrenciaEnvolvidosFilterListView.as_view(),
        name='envolvidonamefilter'),
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
