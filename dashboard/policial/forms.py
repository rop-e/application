from django import forms
from contasdeusuario.models import Usuario
from policial.models import Policial
from django.contrib.auth.forms import UserCreationForm


class FormRegistrarPolicial(forms.ModelForm):
    class Meta:
        model = Policial
        exclude = ["matricula"]


class FormRegistrarUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("__all__")


class FormAtualizarEmail(forms.ModelForm):
    email = forms.EmailField(label="E-mail")

    class Meta:
        model = Usuario
        fields = ["email"]


class FormAtualizarFoto(forms.ModelForm):
    foto = forms.ImageField()

    class Meta:
        model = Policial
        fields = ["foto"]


class FormAtualizarSenha(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = Usuario
        fields = ["password"]
