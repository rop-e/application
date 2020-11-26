from django.urls import path
from .views import (
    AnexoListCreateView,
    AnexoDetailsUpdateDeleteView
)

urlpatterns = [
    path(
        'anexo/',
        AnexoListCreateView.as_view(),
        name='create'),
    path(
        'anexo/<int:pk>/',
        AnexoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
]
