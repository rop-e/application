from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import MatriculaLoginForm
from django.urls import reverse_lazy

app_name = "auth"

urlpatterns = [
    path(
        "entrar/",
        auth_views.LoginView.as_view(
            template_name="auth/login.html",
            authentication_form=MatriculaLoginForm),
        name="entrar"),
    path(
        "sair/",
        auth_views.LogoutView.as_view(
            next_page='index'),
        name="sair"),
    path(
        "esqueci-senha/",
        auth_views.PasswordResetView.as_view(
            template_name="auth/senha_reset_form.html",
            email_template_name="auth/senha_reset_email.html",
            success_url=reverse_lazy(
                'auth:esqueci-senha-ok')),
        name="esqueci-senha"),
    path(
        "esqueci-senha/ok/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="auth/senha_reset_finalizado.html"),
        name="esqueci-senha-ok"),
    path(
        "confirmar-reset-senha/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth/senha_reset_confirmar.html",
            success_url=reverse_lazy(
                'auth:confirmar-reset-senha-ok')),
        name="confirmar-reset-senha"),
    path(
        "confirmar-reset-senha/ok/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth/senha_reset_completo.html"),
        name="confirmar-reset-senha-ok"),
]
