from django import forms
from localrecebedor.models import AgenteRecebedor


class FormEnvolvidoAgenteRecebedor(forms.ModelForm):
    """Formulário para criar Agente Recebedor de Envolvido"""
    class Meta:
        model = AgenteRecebedor
        fields = ["nome_agente", "cargo"]


class FormAcessorioAgenteRecebedor(forms.ModelForm):
    """Formulário para criar Agente Recebedor de Arma"""
    class Meta:
        model = AgenteRecebedor
        fields = ["nome_agente", "cargo"]
