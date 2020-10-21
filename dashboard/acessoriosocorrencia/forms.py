from acessoriosocorrencia.models import (
    TipoArma,
    Arma,
    ArmaAcessorio,
    DrogaAcessorio,
    TipoDroga,
    ArmazenamentoDroga,
    UnidadeMedida,
    TiposDiversos,
    DiversosAcessorio,
    TipoDoc,
    DocAcessorio,
    MunicaoAcessorio,
    Calibre,
    VeiculoAcessorio
)
from localrecebedor.models import LocalRecebedor
from django import forms


class FormArma(forms.ModelForm):
    tipoarma = forms.ModelChoiceField(
               queryset=TipoArma.objects.all(),
               required=False, label="Tipo de arma")

    class Meta:
        model = Arma
        fields = "__all__"

    def clean_tipoarma(self):
        tipoarma = self.cleaned_data["tipoarma"]
        if tipoarma is None:
            raise forms.ValidationError(
                  "É necessário selecionar o tipo de arma!",
                  code="required")
        else:
            return tipoarma


class FormArmaAcessorio(forms.ModelForm):
    localrecebedor = forms.ModelChoiceField(
                     queryset=LocalRecebedor.objects.all(),
                     required=False, label="Local recebedor")

    class Meta:
        model = ArmaAcessorio
        exclude = ["arma", "agenterecebedor", "observacao"]

    def clean_localrecebedor(self):
        localrecebedor = self.cleaned_data["localrecebedor"]
        if localrecebedor is None:
            raise forms.ValidationError(
                  "É necessário selecionar o local recebedor!",
                  code="required")
        else:
            return localrecebedor


class FormDiversosAcessorio(forms.ModelForm):
    localrecebedor = forms.ModelChoiceField(
                     queryset=LocalRecebedor.objects.all(),
                     required=False, label="Local recebedor")
    tipodiversos = forms.ModelChoiceField(
                   queryset=TiposDiversos.objects.all(),
                   required=False, label="Tipo de objeto")

    class Meta:
        model = DiversosAcessorio
        exclude = ["observacao", "agenterecebedor"]

    def clean_localrecebedor(self):
        localrecebedor = self.cleaned_data["localrecebedor"]
        if localrecebedor is None:
            raise forms.ValidationError(
                  "É necessário selecionar o local recebedor!",
                  code="required")
        else:
            return localrecebedor

    def clean_tipodiversos(self):
        tipodiversos = self.cleaned_data["tipodiversos"]
        if tipodiversos is None:
            raise forms.ValidationError(
                  "É necessário selecionar o tipo do item!",
                  code="required")
        else:
            return tipodiversos


class FormEditarDiversosAcessorio(forms.ModelForm):
    tipodiversos = forms.ModelChoiceField(
                   queryset=TiposDiversos.objects.all(),
                   required=False, label="Tipo de objeto")

    class Meta:
        model = DiversosAcessorio
        exclude = [
            "acessoriosocorrencia",
            "observacao",
            "localrecebedor",
            "agenterecebedor"
        ]

    def clean_tipodiversos(self):
        tipodiversos = self.cleaned_data["tipodiversos"]
        if tipodiversos is None:
            raise forms.ValidationError(
                  "É necessário selecionar o tipo do item!",
                  code="required")
        else:
            return tipodiversos


class FormDocAcessorio(forms.ModelForm):
    tipodoc = forms.ModelChoiceField(
              queryset=TipoDoc.objects.all(),
              required=False, label="Tipo de documento")
    localrecebedor = forms.ModelChoiceField(
                     queryset=LocalRecebedor.objects.all(),
                     required=False, label="Local recebedor")

    class Meta:
        model = DocAcessorio
        exclude = ["observacao", "agenterecebedor"]

    def clean_tipodoc(self):
        tipodoc = self.cleaned_data["tipodoc"]
        if tipodoc is None:
            raise forms.ValidationError(
                  "É necessário selecionar o tipo de documento!",
                  code="required")
        else:
            return tipodoc

    def clean_localrecebedor(self):
        localrecebedor = self.cleaned_data["localrecebedor"]
        if localrecebedor is None:
            raise forms.ValidationError(
                  "É necessário selecionar o local recebedor!",
                  code="required")
        else:
            return localrecebedor


class FormEditarDocAcessorio(forms.ModelForm):
    tipodoc = forms.ModelChoiceField(
              queryset=TipoDoc.objects.all(),
              required=False, label="Tipo de documento")

    class Meta:
        model = DocAcessorio
        exclude = [
            "acessoriosocorrencia",
            "observacao",
            "localrecebedor",
            "agenterecebedor"
        ]

    def clean_tipodoc(self):
        tipodoc = self.cleaned_data["tipodoc"]
        if tipodoc is None:
            raise forms.ValidationError(
                  "É necessário selecionar o tipo de documento!",
                  code="required")
        else:
            return tipodoc


class FormDrogaAcessorio(forms.ModelForm):
    localrecebedor = forms.ModelChoiceField(
                     queryset=LocalRecebedor.objects.all(),
                     required=False, label="Local recebedor")
    tipodroga = forms.ModelChoiceField(
                queryset=TipoDroga.objects.all(),
                required=False, label="Tipo de droga")
    armazenamentodroga = forms.ModelChoiceField(
                         queryset=ArmazenamentoDroga.objects.all(),
                         required=False, label="Estado da droga")
    medida = forms.ModelChoiceField(
             queryset=UnidadeMedida.objects.all(),
             required=False, label="Unidade de medida")

    class Meta:
        model = DrogaAcessorio
        exclude = ["observacao", "agenterecebedor"]

    def clean_localrecebedor(self):
        localrecebedor = self.cleaned_data["localrecebedor"]
        if localrecebedor is None:
            raise forms.ValidationError(
                  "É necessário selecionar o local recebedor!",
                  code="required")
        else:
            return localrecebedor

    def clean_tipodroga(self):
        tipodroga = self.cleaned_data["tipodroga"]
        if tipodroga is None:
            raise forms.ValidationError(
                  "É necessário informar qual é a droga!",
                  code="required")
        else:
            return tipodroga

    def clean_armazenamentodroga(self):
        armazenamentodroga = self.cleaned_data["armazenamentodroga"]
        if armazenamentodroga is None:
            raise forms.ValidationError(
                  "É necessário informar o tipo de armazenamento da droga!",
                  code="required")
        else:
            return armazenamentodroga

    def clean_medida(self):
        medida = self.cleaned_data["medida"]
        if medida is None:
            raise forms.ValidationError(
                  "É necessário informar a medida da droga!",
                  code="required")
        else:
            return medida


class FormEditarDrogaAcessorio(forms.ModelForm):
    tipodroga = forms.ModelChoiceField(
                queryset=TipoDroga.objects.all(),
                required=False, label="Tipo de droga")
    armazenamentodroga = forms.ModelChoiceField(
                         queryset=ArmazenamentoDroga.objects.all(),
                         required=False, label="Estado da droga")
    medida = forms.ModelChoiceField(
             queryset=UnidadeMedida.objects.all(),
             required=False, label="Unidade de medida")

    class Meta:
        model = DrogaAcessorio
        exclude = [
            "acessoriosocorrencia",
            "observacao",
            "localrecebedor",
            "agenterecebedor"
        ]

    def clean_tipodroga(self):
        tipodroga = self.cleaned_data["tipodroga"]
        if tipodroga is None:
            raise forms.ValidationError(
                  "É necessário informar qual é a droga!",
                  code="required")
        else:
            return tipodroga

    def clean_armazenamentodroga(self):
        armazenamentodroga = self.cleaned_data["armazenamentodroga"]
        if armazenamentodroga is None:
            raise forms.ValidationError(
                  "É necessário informar o tipo de armazenamento da droga!",
                  code="required")
        else:
            return armazenamentodroga

    def clean_medida(self):
        medida = self.cleaned_data["medida"]
        if medida is None:
            raise forms.ValidationError(
                  "É necessário informar a medida da droga!",
                  code="required")
        else:
            return medida


class FormMunicaoAcessorio(forms.ModelForm):
    localrecebedor = forms.ModelChoiceField(
                     queryset=LocalRecebedor.objects.all(),
                     required=False, label="Local recebedor")
    municao = forms.ModelChoiceField(
              queryset=Calibre.objects.all(),
              required=False, label="Calibre")

    class Meta:
        model = MunicaoAcessorio
        exclude = ["observacao", "agenterecebedor"]

    def clean_localrecebedor(self):
        localrecebedor = self.cleaned_data["localrecebedor"]
        if localrecebedor is None:
            raise forms.ValidationError(
                  "É necessário selecionar o local recebedor!",
                  code="required")
        else:
            return localrecebedor

    def clean_municao(self):
        municao = self.cleaned_data["municao"]
        if municao is None:
            raise forms.ValidationError(
                  "É necessário informar o calibre!",
                  code="required")
        else:
            return municao


class FormEditarMunicaoAcessorio(forms.ModelForm):
    municao = forms.ModelChoiceField(
              queryset=Calibre.objects.all(),
              required=False, label="Calibre")

    class Meta:
        model = MunicaoAcessorio
        exclude = [
            "acessoriosocorrencia",
            "observacao",
            "localrecebedor",
            "agenterecebedor"
        ]

    def clean_municao(self):
        municao = self.cleaned_data["municao"]
        if municao is None:
            raise forms.ValidationError(
                  "É necessário informar o calibre!",
                  code="required")
        else:
            return municao


class FormVeiculoAcessorio(forms.ModelForm):
    localrecebedor = forms.ModelChoiceField(
                     queryset=LocalRecebedor.objects.all(),
                     required=False, label="Local recebedor")

    class Meta:
        model = VeiculoAcessorio
        exclude = ["veiculo", "agenterecebedor", "observacao"]

    def clean_localrecebedor(self):
        localrecebedor = self.cleaned_data["localrecebedor"]
        if localrecebedor is None:
            raise forms.ValidationError(
                  "É necessário selecionar o local recebedor!",
                  code="required")
        else:
            return localrecebedor
