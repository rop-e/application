from django import forms
from ocorrencia.models import (
    Ocorrencia,
    Infracao,
    TipoOcorrencia,
    ObservacaoOcorrencia
)
from django.utils import timezone


class FormOcorrencia(forms.ModelForm):
    """Formulário para criar Ocorrência"""
    tipoocorrencia = forms.ModelChoiceField(
                     queryset=TipoOcorrencia.objects.all(),
                     required=False, label="Tipo de Ocorrência")
    infracao = forms.ModelChoiceField(
               queryset=Infracao.objects.all(),
               required=False, label="Tipo Penal")

    class Meta:
        model = Ocorrencia
        fields = ["tipoocorrencia", "guarnicao", "infracao", "vinculo", "dataocorrencia"]

    def clean_infracao(self):
        infracao = self.cleaned_data["infracao"]
        if infracao is None:
            raise forms.ValidationError(
                "É necessário selecionar o tipo de infração!",
                code="required")
        else:
            return infracao

    def clean_dataocorrencia(self):
        dataocorrencia = self.cleaned_data["dataocorrencia"]
        guarnicao = self.cleaned_data["guarnicao"]
        if dataocorrencia < guarnicao.dataabertura:
            raise forms.ValidationError(
                "Data da Ocorrência menor que a"
                " data de abertura da guarnição!",
                code="date-error-menor")
        if dataocorrencia > timezone.localtime():
            raise forms.ValidationError(
                "Data da Ocorrência maior que a atual!",
                code="date-error-maior")
        else:
            return dataocorrencia


class FormEditarRelatorio(forms.ModelForm):
    """Formulário para editar Relatório da Ocorrência"""
    class Meta:
        model = Ocorrencia
        fields = ["relatorio"]

    def clean_relatorio(self):
        relatorio = self.cleaned_data["relatorio"]
        if relatorio == "":
            raise forms.ValidationError(
                "É necessário informar o relatório da ocorrência!",
                code="required")
        else:
            return relatorio


class FormObservacaoOcorrencia(forms.ModelForm):
    """Formulário para criar Aditamento"""
    class Meta:
        model = ObservacaoOcorrencia
        exclude = ["observacao", "ativo", "autor"]
