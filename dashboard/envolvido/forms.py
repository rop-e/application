from django import forms
from envolvido.models import (
    Envolvido,
    TipoEnvolvimento
)
from localrecebedor.models import LocalRecebedor


class FormEnvolvido(forms.ModelForm):
    """Formulário para criar Envolvido"""
    tipoenvolvimento = forms.ModelChoiceField(
                    queryset=TipoEnvolvimento.objects.filter(rat=False),
                    required=False, label="Tipo de envolvimento")
    localrecebedor = forms.ModelChoiceField(
                     queryset=LocalRecebedor.objects.all(),
                     required=False, label="Local recebedor")

    class Meta:
        model = Envolvido
        exclude = ["pessoa", "agenterecebedor", "observacao"]

    def clean_tipoenvolvimento(self):
        tipoenvolvimento = self.cleaned_data["tipoenvolvimento"]
        if tipoenvolvimento is None:
            raise forms.ValidationError(
                  "É necessário selecionar o tipo do envolvimento!",
                  code="required")
        else:
            return tipoenvolvimento


class FormEnvolvidoRAT(forms.ModelForm):
    """Formulário para criar Envolvido em RAT"""
    tipoenvolvimento = forms.ModelChoiceField(
                    queryset=TipoEnvolvimento.objects.filter(rat=True),
                    required=False, label="Tipo de envolvimento")
    localrecebedor = forms.ModelChoiceField(
                     queryset=LocalRecebedor.objects.all(),
                     required=False, label="Local recebedor")

    class Meta:
        model = Envolvido
        exclude = ["pessoa", "agenterecebedor", "observacao"]

    def clean_tipoenvolvimento(self):
        tipoenvolvimento = self.cleaned_data["tipoenvolvimento"]
        if tipoenvolvimento is None:
            raise forms.ValidationError(
                  "É necessário selecionar o tipo do envolvimento!",
                  code="required")
        else:
            return tipoenvolvimento


class FormEditarEnvolvidoOcorrencia(forms.ModelForm):
    """Formulário para editar Envolvido"""
    tipoenvolvimento = forms.ModelChoiceField(
                       queryset=TipoEnvolvimento.objects.filter(rat=False),
                       required=False, label="Tipo de envolvimento")

    class Meta:
        model = Envolvido
        exclude = ["ocorrencia", "localrecebedor", "agenterecebedor"]

    def clean_tipoenvolvimento(self):
        tipoenvolvimento = self.cleaned_data["tipoenvolvimento"]
        if tipoenvolvimento is None:
            raise forms.ValidationError(
                  "É necessário selecionar o tipo do envolvimento!",
                  code="required")
        else:
            return tipoenvolvimento


class FormEditarEnvolvidoRAT(forms.ModelForm):
    """Formulário para editar Envolvido"""
    tipoenvolvimento = forms.ModelChoiceField(
                       queryset=TipoEnvolvimento.objects.filter(rat=True),
                       required=False, label="Tipo de envolvimento")

    class Meta:
        model = Envolvido
        exclude = ["rat", "localrecebedor", "agenterecebedor"]

    def clean_tipoenvolvimento(self):
        tipoenvolvimento = self.cleaned_data["tipoenvolvimento"]
        if tipoenvolvimento is None:
            raise forms.ValidationError(
                  "É necessário selecionar o tipo do envolvimento!",
                  code="required")
        else:
            return tipoenvolvimento
