from django import forms
from observacao.models import Observacao


class FormObservacao(forms.ModelForm):
    class Meta:
        model = Observacao
        fields = ["observacao"]
