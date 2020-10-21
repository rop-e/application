from django.urls import path
from .endereco_views import (
    index,
    edit_endereco,
    post_edit_endereco
)

app_name = 'endereco'

urlpatterns = [
    path('', index, name='index'),
    path('<str:codigo_ibge>/', index),
    path(
        "editar/endereco/<int:id>/",
        edit_endereco, name="edit_endereco"),
    path(
        "editar/endereco/post/ajax/",
        post_edit_endereco, name="post_edit_endereco"),
]
