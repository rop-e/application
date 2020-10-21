from django.urls import path
from .views import (
        ProcedimentoOcorrenciaListCreateView,
        ProcedimentoOcorrenciaDetailsUpdateDeleteView
    )
urlpatterns = [
    path(
         '',
         ProcedimentoOcorrenciaListCreateView.as_view(),
         name='create'),
    path(
         '<int:pk>/',
         ProcedimentoOcorrenciaDetailsUpdateDeleteView.as_view(),
         name='detalhe'),
]
