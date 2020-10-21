from django.urls import path
from .views import (
        ObservacaoListCreateView,
        ObservacaoDetailsUpdateDeleteView
    )
urlpatterns = [
    path(
         '',
         ObservacaoListCreateView.as_view(),
         name='create'),
    path(
         '<int:pk>/',
         ObservacaoDetailsUpdateDeleteView.as_view(),
         name='detalhe'),
]
