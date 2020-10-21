from django.urls import path
from .views import (
    LocalRecebedorListCreateView,
    LocalRecebedorDetailsUpdateDeleteView,
    AgenteRecebedorListCreateView,
    AgenteRecebedorDetailsUpdateDeleteView
)

urlpatterns = [
    path(
        '',
        LocalRecebedorListCreateView.as_view(),
        name='create'),
    path(
        '<int:pk>/',
        LocalRecebedorDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        'agenterecebedor/',
        AgenteRecebedorListCreateView.as_view(),
        name='create'),
    path(
        'agenterecebedor/<int:pk>/',
        AgenteRecebedorDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
]
