from django import forms
from veiculo.models import (
    CategoriaVeiculo,
    MarcaVeiculo,
    Veiculo
)


class FormVeiculo(forms.ModelForm):
    categoria = forms.ModelChoiceField(
                queryset=CategoriaVeiculo.objects.filter(),
                required=False, label="Categoria")
    marca = forms.ModelChoiceField(
            queryset=MarcaVeiculo.objects.filter(),
            required=False, label="Marca")

    class Meta:
        model = Veiculo
        fields = ("__all__")

    def clean_categoria(self):
        categoria = self.cleaned_data["categoria"]
        if categoria is None:
            raise forms.ValidationError(
                  "É necessário selecionar uma categoria!",
                  code="required")
        else:
            return categoria

    def clean_marca(self):
        marca = self.cleaned_data["marca"]
        if marca is None:
            raise forms.ValidationError(
                  "É necessário selecionar uma marca!",
                  code="required")
        else:
            return marca
