from django import forms
from opo.models import (
    OPO,
    OPOTipoEvento,
    OPORelatorio,
    OPOComandantesCIA
)
from policial.models import Policial
from guarnicao.models import Guarnicao
from django.forms import ModelChoiceField

STATUS_RELATORIO = (
    ("", "---------"),
    ("pendente", "PENDENTE"),
    ("andamento", "EM ANDAMENTO"),
    ("finalizada", "FINALIZADA")
)

DESIGNADO_PARA = (
    ("", "---------"),
    ("coordenadordearea", "COORDENADOR DE ÁREA"),
    ("cicom", "CICOM"),
    ("comandantecia", "COMANDANTE DE CIA")
)


class FormOPO(forms.ModelForm):
    opotipoevento = forms.ModelChoiceField(
                    queryset=OPOTipoEvento.objects.all(),
                    required=False, label="Tipo de evento")
    designado = forms.ChoiceField(choices=DESIGNADO_PARA, required=False, label="Designado para")

    class Meta:
        model = OPO
        exclude = ["observacao"]

    def clean(self):
        cleaned_data = super().clean()
        datasolicitacao = cleaned_data.get('datasolicitacao')
        datainicio = cleaned_data.get('datainicio')
        datatermino = cleaned_data.get('datatermino')
        opotipoevento = cleaned_data.get('opotipoevento')
        designado = cleaned_data.get('designado')

        if datainicio < datasolicitacao:
            raise forms.ValidationError(
                "Data de início da OPO menor que a"
                " data de solicitação da mesma!",
                code="date-inicio-error-menor")
        
        if datatermino:
            if datatermino < datasolicitacao:
                raise forms.ValidationError(
                    "Data de término da OPO menor que a"
                    " data de solicitação da mesma!",
                    code="date-termino-error-menor")
            if datatermino < datainicio:
                raise forms.ValidationError(
                    "Data de término da OPO menor que a"
                    " data de início da mesma!",
                    code="date-termino-error-menor-inicio")
        
        if opotipoevento is None:
            raise forms.ValidationError(
                "É necessário selecionar o tipo de evento!",
                code="required")

        if designado == "":
            raise forms.ValidationError(
                  "É necessário designar a OPO!",
                  code="required")

        return cleaned_data


class FormDadosOPO(forms.ModelForm):
    opotipoevento = forms.ModelChoiceField(
                    queryset=OPOTipoEvento.objects.all(),
                    required=False, label="Tipo de evento")

    class Meta:
        model = OPO
        fields = ["opotipoevento", "titulo", "datasolicitacao", "numeroopo", "armamento", "uniforme"]

    def clean(self):
        cleaned_data = super().clean()
        opotipoevento = cleaned_data.get('opotipoevento')

        if opotipoevento is None:
            raise forms.ValidationError(
                "É necessário selecionar o tipo de evento!",
                code="required")

        return cleaned_data


class FormSolicitacaoOPO(forms.ModelForm):
    designado = forms.ChoiceField(choices=DESIGNADO_PARA, required=False, label="Designado para")

    class Meta:
        model = OPO
        fields = ["solicitantenome", "solicitantecontato", "datainicio", "datatermino", "local", "designado"]

    def clean(self):
        cleaned_data = super().clean()
        designado = cleaned_data.get('designado')

        if designado == "":
            raise forms.ValidationError(
                  "É necessário designar a OPO!",
                  code="required")
        
        return cleaned_data


class FormCreateOPORelatorio(forms.ModelForm):
    class Meta:
        model = OPORelatorio
        exclude = ["guarnicao", "designador", "status", "relatorio"]

    def clean(self):
        cleaned_data = super().clean()
        dataexecucao = cleaned_data.get('dataexecucao')
        datafinalizacao = cleaned_data.get('datafinalizacao')
        opo = cleaned_data.get('opo')

        if dataexecucao < opo.datainicio:
            raise forms.ValidationError(
                "Data de execução menor que a"
                " data de início da mesma!",
                code="date-execucao-error-menor-inicio")
        
        if opo.datatermino:
            if dataexecucao > opo.datatermino:
                raise forms.ValidationError(
                    "Data de execução maior que a"
                    " data de término da mesma!",
                    code="date-execucao-error-maior-termino")
        
        if datafinalizacao:
            if dataexecucao > datafinalizacao:
                raise forms.ValidationError(
                    "Data de execução maior que a"
                    " data de finalização da mesma!",
                    code="date-execucao-error-maior-finalizacao")
            if datafinalizacao < dataexecucao:
                raise forms.ValidationError(
                    "Data de finalização menor que a"
                    " data de execução da mesma!",
                    code="date-finalizacao-error-menor-execucao")
            if datafinalizacao > opo.datatermino:
                raise forms.ValidationError(
                    "Data de finalização maior que a"
                    " data de término da mesma!",
                    code="date-finalizacao-error-maior-termino")

        return cleaned_data


class ComandanteCiaChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.postograduacao} {obj.nomeguerra} - {obj.companhia}"


class FormCreateOPOComandantesCIA(forms.ModelForm):
    comandante = ComandanteCiaChoiceField(
                 queryset=Policial.objects.filter(
                     comandante_companhia__isnull=False),
                 required=False, label="Comandante de CIA")

    class Meta:
        model = OPOComandantesCIA
        fields = ("__all__")

    def clean(self):
        cleaned_data = super(FormCreateOPOComandantesCIA, self).clean()
        comandante = cleaned_data['comandante']

        if comandante is None:
            raise forms.ValidationError(
                "Informe um comandante de CIA!",
                code="required")
        
        return cleaned_data


class FormCPOEditSubOPO(forms.ModelForm):
    class Meta:
        model = OPORelatorio
        fields = ["opo", "local", "dataexecucao", "datafinalizacao"]
    
    def clean(self):
        cleaned_data = super(FormCPOEditSubOPO, self).clean()
        dataexecucao = cleaned_data['dataexecucao']
        datafinalizacao = cleaned_data['datafinalizacao']
        opo = cleaned_data['opo']

        if dataexecucao < opo.datainicio:
            raise forms.ValidationError(
                "Data de execução menor que a"
                " data de início da mesma!",
                code="date-execucao-error-menor-inicio")
        
        if opo.datatermino:
            if dataexecucao > opo.datatermino:
                raise forms.ValidationError(
                    "Data de execução maior que a"
                    " data de término da mesma!",
                    code="date-execucao-error-maior-termino")
        
        if datafinalizacao:
            if dataexecucao > datafinalizacao:
                raise forms.ValidationError(
                    "Data de execução maior que a"
                    " data de finalização da mesma!",
                    code="date-execucao-error-maior-finalizacao")
            if datafinalizacao < dataexecucao:
                raise forms.ValidationError(
                    "Data de finalização menor que a"
                    " data de execução da mesma!",
                    code="date-finalizacao-error-menor-execucao")
            if datafinalizacao > opo.datatermino:
                raise forms.ValidationError(
                    "Data de finalização maior que a"
                    " data de término da mesma!",
                    code="date-finalizacao-error-maior-termino")

        return cleaned_data


class FormEditOPORelatorio(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_RELATORIO, required=False)

    class Meta:
        model = OPORelatorio
        fields = ["status", "relatorio"]

    def clean_status(self):
        status = self.cleaned_data["status"]
        if status == "":
            raise forms.ValidationError(
                  "É necessário escolher o status!",
                  code="required")
        else:
            return status
