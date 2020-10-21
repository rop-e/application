from django import forms
from pessoa.models import Pessoa

SEXO = (
    ("", "---------"),
    ("M", "MASCULINO"),
    ("F", "FEMININO")
)


class FormPessoa(forms.ModelForm):
    """Formulário para criar Pessoa"""
    sexo = forms.ChoiceField(choices=SEXO, required=False)

    class Meta:
        model = Pessoa
        fields = ("__all__")

    def clean_sexo(self):
        sexo = self.cleaned_data["sexo"]
        if sexo == "":
            raise forms.ValidationError(
                  "É necessário escolher o sexo!",
                  code="required")
        else:
            return sexo
