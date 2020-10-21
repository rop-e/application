from anexo.models import Anexo
from django import forms


class FormAnexoRAT(forms.ModelForm):
    class Meta:
        model = Anexo
        exclude = ["ocorrencia", "observacao"]


class FormAnexoOcorrencia(forms.ModelForm):
    class Meta:
        model = Anexo
        exclude = ["rat", "observacao"]
