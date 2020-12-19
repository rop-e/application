from rest_framework import serializers
from .models import (
    Ocorrencia,
    TipoOcorrencia,
    Infracao,
    ObservacaoOcorrencia
)
from guarnicao.models import Guarnicao
from policial.models import Policial
from endereco.models import (
    Endereco,
    Municipios,
    Estados
)

class TipoOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOcorrencia
        fields = ("__all__")


class InfracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infracao
        fields = ("__all__")


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ObservacaoOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservacaoOcorrencia
        fields = ("__all__")


class ListOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ("__all__")
        depth = 2


class ListObservacaoOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservacaoOcorrencia
        fields = ("__all__")
        depth = 2


class VinculoOcorrenciaFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ["id"]


class TipoOcorrenciaFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOcorrencia
        fields = ["tipoocorrencia"]


class InfracaoFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infracao
        fields = ["tipo"]


class EstadosFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        fields = ["uf"]


class MunicipiosFilterSerializer(serializers.ModelSerializer):
    codigo_uf = EstadosFilterSerializer()

    class Meta:
        model = Municipios
        fields = ["nome", "codigo_uf"]


class EnderecoFilterSerializer(serializers.ModelSerializer):
    municipio = MunicipiosFilterSerializer()

    class Meta:
        model = Endereco
        exclude = ["id", "datacriacao", "dataatualizacao", "latitude", "longitude", "observacao"]


class PolicialFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policial
        fields = ["nomeguerra"]


class GuarnicaoFilterSerializer(serializers.ModelSerializer):
    comandante = PolicialFilterSerializer()
    class Meta:
        model = Guarnicao
        fields = ["comandante"]


class ListOcorrenciaFilterSerializer(serializers.ModelSerializer):
    guarnicao = GuarnicaoFilterSerializer()
    endereco = EnderecoFilterSerializer()
    infracao = InfracaoFilterSerializer()
    tipoocorrencia = TipoOcorrenciaFilterSerializer()
    vinculo = VinculoOcorrenciaFilterSerializer()

    class Meta:
        model = Ocorrencia
        exclude = ["status_previa", "datacriacao", "dataatualizacao"]
        depth = 2
