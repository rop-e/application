from django.urls import path
from .views import (
    OcorrenciaListCreateView,
    OcorrenciaDetailsUpdateDeleteView,
    TipoInfracaoListCreateView,
    TipoOcorrenciaListCreateView,
    OcorrenciaDateFilterListView,
    OcorrenciaEnvolvidosFilterListView,
    OrgaoListCreateView,
    OrgaoDetailsUpdateDeleteView,
    OcorrenciasGuarnicaoListView,
    ApreensoesOcorrenciaListView
)

urlpatterns = [
    path(
        '',
        OcorrenciaListCreateView.as_view(),
        name='create'),
    path(
        'guarnicao/<int:id>/',
        OcorrenciasGuarnicaoListView.as_view(),
        name='ocorrencias_guarnicao'),
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
        'apreensoes/<int:pk>/',
        ApreensoesOcorrenciaListView.as_view(),
        name='apreensoes'),
    path(
        'tipoinfracao/',
        TipoInfracaoListCreateView.as_view(),
        name='create'),
    path(
        'tipoocorrencia/',
        TipoOcorrenciaListCreateView.as_view(),
        name='create'),
    path(
        'orgao/',
        OrgaoListCreateView.as_view(),
        name='create'),
    path(
        'orgao/<int:pk>/',
        OrgaoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
]
