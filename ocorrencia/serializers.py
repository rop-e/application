from rest_framework import serializers
from .models import (
    Ocorrencia,
    TipoOcorrencia,
    Infracao,
    ObservacaoOcorrencia
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
