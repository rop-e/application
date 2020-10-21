from django.urls import path
from .views import (
    PolicialViaturaListCreateView,
    PolicialViaturaDetailsUpdateDeleteView,
    FuncaoDetailsUpdateDeleteView,
    FuncaoListCreateView
)

urlpatterns = [
    path(
        '',
        PolicialViaturaListCreateView.as_view(),
        name='create'),
    path(
        '<int:pk>/',
        PolicialViaturaDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        'funcao/',
        FuncaoListCreateView.as_view(),
        name='create'),
    path(
        'funcao/<int:pk>/',
        FuncaoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
]
