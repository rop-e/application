from rest_framework import serializers
from .models import ProcedimentoOcorrencia, Procedimento
from ocorrencia.serializers import OcorrenciaSerializer
from observacao.serializers import ObservacaoSerializer


class ProcedimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Procedimento
        fields = ('procedimento',)


class ProcedimentoOcorrenciaSerializer(serializers.ModelSerializer):
    procedimento = ProcedimentoSerializer()
    ocorrencia = OcorrenciaSerializer()
    observacao = ObservacaoSerializer()

    class Meta:
        model = ProcedimentoOcorrencia
        fields = (
            'id',
            'procedimento',
            'ocorrencia',
            'observacao',
            )
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )
