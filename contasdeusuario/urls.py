from .views import AlteracaoSenhaView
from django.urls import (
    path,
    include
)

urlpatterns = [
    path("alterar-senha/", AlteracaoSenhaView.as_view(), name="alterar-senha"),
    path("resetar-senha/", include("django_rest_passwordreset.urls", namespace="resetar-senha"))
]