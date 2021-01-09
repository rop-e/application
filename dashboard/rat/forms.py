from django import forms
from rat.models import (
    RAT,
    TipoAcidente,
    CondicaoSinalizacao,
    CondicaoVia,
    CondicaoMeteorologica,
    Pavimentacao,
    TracadoVia,
    RATObjetos,
    RATVeiculoEnvolvidos,
    RATVeiculos
)
from django.utils import timezone


class FormRAT(forms.ModelForm):
    tipoacidente = forms.ModelChoiceField(
                   queryset=TipoAcidente.objects.all(),
                   required=False, label="Tipo de acidente")
    condicaosinalizacao = forms.ModelChoiceField(
                          queryset=CondicaoSinalizacao.objects.all(),
                          required=False, label="Condição da sinalização")
    condicaovia = forms.ModelChoiceField(
                  queryset=CondicaoVia.objects.all(),
                  required=False, label="Condição da via")
    condicaometeorologica = forms.ModelChoiceField(
                            queryset=CondicaoMeteorologica.objects.all(),
                            required=False, label="Condição meteorológica")
    pavimentacao = forms.ModelChoiceField(
                   queryset=Pavimentacao.objects.all(),
                   required=False, label="Tipo de pavimentação")
    tracadovia = forms.ModelChoiceField(
                 queryset=TracadoVia.objects.all(),
                 required=False, label="Traçado da via")

    class Meta:
        model = RAT
        exclude = ["endereco", "relatorio", "hash", "status_previa"]

    def clean(self):
        cleaned_data = super(FormRAT, self).clean()
        tipoacidente = cleaned_data['tipoacidente']
        condicaosinalizacao = cleaned_data['condicaosinalizacao']
        condicaovia = cleaned_data['condicaovia']
        condicaometeorologica = cleaned_data['condicaometeorologica']
        pavimentacao = cleaned_data['pavimentacao']
        tracadovia = cleaned_data['tracadovia']
        dataocorrencia = cleaned_data['dataocorrencia']
        guarnicao = cleaned_data['guarnicao']

        if tipoacidente is None:
            raise forms.ValidationError(
                "É necessário selecionar o tipo de acidente!",
                code="required")
        if condicaosinalizacao is None:
            raise forms.ValidationError(
                "É necessário selecionar a condição da sinalização!",
                code="required")
        if condicaovia is None:
            raise forms.ValidationError(
                "É necessário selecionar a condição da via!",
                code="required")
        if condicaometeorologica is None:
            raise forms.ValidationError(
                "É necessário selecionar a condição meteorológica!",
                code="required")
        if pavimentacao is None:
            raise forms.ValidationError(
                "É necessário selecionar o tipo de pavimentação!",
                code="required")
        if tracadovia is None:
            raise forms.ValidationError(
                "É necessário selecionar o traçado da via!",
                code="required")
        if dataocorrencia < guarnicao.dataabertura:
            raise forms.ValidationError(
                "Data da RAT menor que a"
                " data de abertura da guarnição!",
                code="date-error-menor")
        if dataocorrencia > timezone.localtime():
            raise forms.ValidationError(
                "Data da RAT maior que a atual!",
                code="date-error-maior")

        return cleaned_data


class FormEditarRAT(forms.ModelForm):
    tipoacidente = forms.ModelChoiceField(
                   queryset=TipoAcidente.objects.all(),
                   required=False, label="Tipo de acidente")
    condicaosinalizacao = forms.ModelChoiceField(
                          queryset=CondicaoSinalizacao.objects.all(),
                          required=False, label="Condição da sinalização")
    condicaovia = forms.ModelChoiceField(
                  queryset=CondicaoVia.objects.all(),
                  required=False, label="Condição da via")
    condicaometeorologica = forms.ModelChoiceField(
                            queryset=CondicaoMeteorologica.objects.all(),
                            required=False, label="Condição meteorológica")
    pavimentacao = forms.ModelChoiceField(
                   queryset=Pavimentacao.objects.all(),
                   required=False, label="Tipo de pavimentação")
    tracadovia = forms.ModelChoiceField(
                 queryset=TracadoVia.objects.all(),
                 required=False, label="Traçado da via")

    class Meta:
        model = RAT
        exclude = ["endereco", "relatorio", "guarnicao", "endereco", "dataocorrencia", "hash", "status_previa"]
    
    def clean(self):
        cleaned_data = super(FormEditarRAT, self).clean()
        tipoacidente = cleaned_data['tipoacidente']
        condicaosinalizacao = cleaned_data['condicaosinalizacao']
        condicaovia = cleaned_data['condicaovia']
        condicaometeorologica = cleaned_data['condicaometeorologica']
        pavimentacao = cleaned_data['pavimentacao']
        tracadovia = cleaned_data['tracadovia']

        if tipoacidente is None:
            raise forms.ValidationError(
                "É necessário selecionar o tipo de acidente!",
                code="required")
        if condicaosinalizacao is None:
            raise forms.ValidationError(
                "É necessário selecionar a condição da sinalização!",
                code="required")
        if condicaovia is None:
            raise forms.ValidationError(
                "É necessário selecionar a condição da via!",
                code="required")
        if condicaometeorologica is None:
            raise forms.ValidationError(
                "É necessário selecionar a condição meteorológica!",
                code="required")
        if pavimentacao is None:
            raise forms.ValidationError(
                "É necessário selecionar o tipo de pavimentação!",
                code="required")
        if tracadovia is None:
            raise forms.ValidationError(
                "É necessário selecionar o traçado da via!",
                code="required")

        return cleaned_data


class FormEditarRelatorio(forms.ModelForm):
    class Meta:
        model = RAT
        fields = ["relatorio"]

    def clean_relatorio(self):
        relatorio = self.cleaned_data["relatorio"]
        if relatorio == "":
            raise forms.ValidationError(
                "É necessário informar o relatório da ocorrência!",
                code="required")
        else:
            return relatorio


class FormRATObjetos(forms.ModelForm):
    class Meta:
        model = RATObjetos
        fields = ("__all__")


class FormEditarRATObjetos(forms.ModelForm):
    class Meta:
        model = RATObjetos
        exclude = ["rat"]


class FormRATVeiculos(forms.ModelForm):
    class Meta:
        model = RATVeiculos
        exclude = ["veiculo", "agenterecebedor", "observacao"]


class FormEditarRATVeiculos(forms.ModelForm):
    class Meta:
        model = RATVeiculos
        exclude = ["rat"]


class FormRATVeiculoEnvolvidos(forms.ModelForm):
    class Meta:
        model = RATVeiculoEnvolvidos
        exclude = ["envolvido"]
