from django.urls import path
from .views import (
    PessoaListCreateView,
    PessoaDetailsUpdateDeleteView,
    PessoaEnderecoListCreateView,
    PessoaEnderecoDetailsUpdateDeleteView
)

urlpatterns = [
    path(
        '',
        PessoaListCreateView.as_view(),
        name='create'),
    path(
        '<int:pk>/',
        PessoaDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        'endereco/',
        PessoaEnderecoListCreateView.as_view(),
        name='create'),
    path(
        'endereco/<int:pk>/',
        PessoaEnderecoDetailsUpdateDeleteView.as_view(),
        name='detalhe')
]
