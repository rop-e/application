from django.urls import path
from .views import (
        PolicialListCreateView,
        PolicialDetailsUpdateDeleteView
    )
urlpatterns = [
    path(
         '',
         PolicialListCreateView.as_view(),
         name='create'),
    path(
         '<int:pk>/',
         PolicialDetailsUpdateDeleteView.as_view(),
         name='detalhe'),
]
