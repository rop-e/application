from django.urls import path
from .views import (
    EstadosListCreateView,
    EstadosDetailsUpdateDeleteView,
    MunicipiosListCreateView,
    MunicipiosDetailsUpdateDeleteView,
    EnderecoListCreateView,
    EnderecoDetailsUpdateDeleteView,
)

urlpatterns = [
    path(
        'estados/',
        EstadosListCreateView.as_view(),
        name='create'),
    path(
        'estados/<int:pk>/',
        EstadosDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        'municipios/',
        MunicipiosListCreateView.as_view(),
        name='create'),
    path(
        'municipios/<int:pk>/',
        MunicipiosDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        'endereco/',
        EnderecoListCreateView.as_view(),
        name='create'),
    path(
        'endereco/<int:pk>/',
        EnderecoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
]
