from django.urls import path
from .views import (
    BatalhaoListCreateView,
    BatalhaoDetailsUpdateDeleteView,
    BatalhaoMunicipiosListCreateView,
    BatalhaoMunicipiosDetailsUpdateDeleteView
)

urlpatterns = [
    path(
        '',
        BatalhaoListCreateView.as_view(),
        name='create'),
    path(
        '<int:pk>/',
        BatalhaoDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
    path(
        'batalhaomunicipios/',
        BatalhaoMunicipiosListCreateView.as_view(),
        name='create'),
    path(
        'batalhaomunicipios/<int:pk>/',
        BatalhaoMunicipiosDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
]
