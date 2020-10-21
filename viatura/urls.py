from django.urls import path
from .views import (
    ViaturaListCreateView,
    ViaturaDetailsUpdateDeleteView
)

urlpatterns = [
    path(
        '',
        ViaturaListCreateView.as_view(),
        name='create'),
    path(
        '<int:pk>/',
        ViaturaDetailsUpdateDeleteView.as_view(),
        name='detalhe'),
]
