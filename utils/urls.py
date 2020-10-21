from django.urls import path
from .gerar_pdf import GerarPDF

urlpatterns = [
    path(
        'gerarpdf/',
        GerarPDF,
        name='gerarpdf'),
]
