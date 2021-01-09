from django import forms
from guarnicao.models import (
    Guarnicao,
    Companhia,
    TipoServico,
    ModalidadedePoliciamento,
    GuarnicaoAIT,
    GuarnicaoRRD,
    GuarnicaoTRAV
)
from endereco.models import Municipios
from policial.models import Policial

TIPO_VEICULO = (
    ("", "---------"),
    ('carro', 'CARRO'),
    ('moto', 'MOTO')
)


class FormCompanhia(forms.ModelForm):
    class Meta:
        model = Companhia
        fields = ["companhia"]


class FormGuarnicao(forms.ModelForm):
    """Formulário para criar Guarnição"""
    tiposervico = forms.ModelChoiceField(
                  queryset=TipoServico.objects.all(),
                  required=False, label="Tipo de serviço")
    modalidadepoliciamento = forms.ModelChoiceField(
                             queryset=ModalidadedePoliciamento.objects.all(),
                             required=False,
                             label="Modalidade de policiamento")
    companhia = forms.ModelChoiceField(
                queryset=Companhia.objects.all(),
                required=False, label="Companhia")
    coordenadordearea = forms.ModelChoiceField(
                        queryset=Policial.objects.filter(
                            cargo__cargo="COORDENADOR DE ÁREA"),
                        required=False, label="Coordenador de área")

    def __init__(self, request, *args, **kwargs):
        super(FormGuarnicao, self).__init__(*args, **kwargs)

        self.fields['municipio'].queryset =\
            Municipios.objects.filter(
                batalhaomunicipios__batalhao=request.user.policial.batalhao).order_by(
                'batalhaomunicipios__municipio__nome')
        self.fields['municipio'].required = False
        self.fields['municipio'].label = "Município atuante"

    class Meta:
        model = Guarnicao
        exclude = ["comandante", "relatorio", "ativo", "bloqueadopor", "observacao", "hash"]

    def clean_tiposervico(self):
        tiposervico = self.cleaned_data["tiposervico"]
        if tiposervico is None:
            raise forms.ValidationError(
                  "É necessário selecionar o tipo de serviço!",
                  code="required")
        else:
            return tiposervico

    def clean_modalidadepoliciamento(self):
        modalidadepoliciamento = self.cleaned_data["modalidadepoliciamento"]
        if modalidadepoliciamento is None:
            raise forms.ValidationError(
                  "É necessário selecionar a modalidade de policiamento!",
                  code="required")
        else:
            return modalidadepoliciamento

    def clean_companhia(self):
        companhia = self.cleaned_data["companhia"]
        if companhia is None:
            raise forms.ValidationError(
                  "É necessário selecionar a companhia!",
                  code="required")
        else:
            return companhia

    def clean_municipio(self):
        municipio = self.cleaned_data["municipio"]
        if municipio is None:
            raise forms.ValidationError(
                  "É necessário selecionar o município atuante!",
                  code="required")
        else:
            return municipio
    
    def clean_coordenadordearea(self):
        coordenadordearea = self.cleaned_data["coordenadordearea"]
        if coordenadordearea is None:
            raise forms.ValidationError(
                  "É necessário selecionar o coordenador de área!",
                  code="required")
        else:
            return coordenadordearea


class FormGuarnicaoAIT(forms.ModelForm):
    tipoveiculo = forms.ChoiceField(
                  choices=TIPO_VEICULO, required=False,
                  label='Tipo de veículo')

    class Meta:
        model = GuarnicaoAIT
        fields = ("__all__")
    
    def clean_tipoveiculo(self):
        tipoveiculo = self.cleaned_data["tipoveiculo"]
        if tipoveiculo == "":
            raise forms.ValidationError(
                  "É necessário escolher o típo de veículo!",
                  code="required")
        else:
            return tipoveiculo


class FormGuarnicaoRRD(forms.ModelForm):
    tipoveiculo = forms.ChoiceField(
                  choices=TIPO_VEICULO, required=False,
                  label='Tipo de veículo')

    class Meta:
        model = GuarnicaoRRD
        fields = ("__all__")

    def clean_tipoveiculo(self):
        tipoveiculo = self.cleaned_data["tipoveiculo"]
        if tipoveiculo == "":
            raise forms.ValidationError(
                  "É necessário escolher o típo de veículo!",
                  code="required")
        else:
            return tipoveiculo

class FormGuarnicaoTRAV(forms.ModelForm):
    tipoveiculo = forms.ChoiceField(
                  choices=TIPO_VEICULO, required=False,
                  label='Tipo de veículo')

    class Meta:
        model = GuarnicaoTRAV
        fields = ("__all__")

    def clean_tipoveiculo(self):
        tipoveiculo = self.cleaned_data["tipoveiculo"]
        if tipoveiculo == "":
            raise forms.ValidationError(
                  "É necessário escolher o típo de veículo!",
                  code="required")
        else:
            return tipoveiculo
