from django import forms
from policial.models import Policial
from policialviatura.models import (
    PolicialViatura,
    Funcao
)


class FormPolicialViatura(forms.ModelForm):
    funcao = forms.ModelChoiceField(
             queryset=Funcao.objects.all(),
             required=False, label="Função")

    class Meta:
        model = PolicialViatura
        fields = [
            "policial",
            "funcao",
            "viatura",
            "guarnicao",
            "kmsaida",
            "kmvolta"
        ]

    def clean_funcao(self):
        funcao = self.cleaned_data["funcao"]
        if funcao is None:
            raise forms.ValidationError(
                  "É necessário selecionar a função!",
                  code="required")
        else:
            return funcao
