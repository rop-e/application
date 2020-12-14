from django.urls import path
from .views import (
    PolicialListCreateView,
    PolicialDetailsUpdateDeleteView,
    PolicialUsuarioView
)

urlpatterns = [
    path(
        'usuario/<int:id>/',
        PolicialUsuarioView.as_view(),
        name='usuario'
    ),
    path(
         '',
         PolicialListCreateView.as_view(),
         name='create'),
    path(
         '<int:pk>/',
         PolicialDetailsUpdateDeleteView.as_view(),
         name='detalhe'),
]
