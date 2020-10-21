from django import forms
from endereco.models import (
    Municipios,
    Endereco
)


class FormEndereco(forms.ModelForm):
    municipio = forms.ModelChoiceField(
                queryset=Municipios.objects.filter(
                    batalhaomunicipios__batalhao__batalhao="17º BPM").order_by(
                        'batalhaomunicipios__municipio__nome'),
                required=False, label="Município")

    class Meta:
        model = Endereco
        exclude = ["observacao", "latitude", "longitude"]

    def clean_municipio(self):
        municipio = self.cleaned_data["municipio"]
        if municipio is None:
            raise forms.ValidationError(
                  "É necessário selecionar um município!",
                  code="required")
        else:
            return municipio
