from rest_framework import serializers
from .models import (
    Guarnicao,
    Companhia,
    TipoServico,
    ModalidadedePoliciamento,
    GuarnicaoAIT,
    GuarnicaoRRD,
    GuarnicaoTRAV,
    Permuta
)
from policial.models import Policial


class CompanhiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companhia
        fields = ("__all__")


class TipoServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServico
        fields = ("__all__")


class ModalidadedePoliciamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadedePoliciamento
        fields = ("__all__")


class GuarnicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarnicao
        fields = ("__all__")
        read_only_fields = (
            'dataabertura',
            'dataatualizacao',
        )


class GuarnicaoAITSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarnicaoAIT
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class GuarnicaoRRDSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarnicaoRRD
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class GuarnicaoTRAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarnicaoTRAV
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class AtivaGuarnicaoAITSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarnicaoAIT
        exclude = ["guarnicao", "dataatualizacao"]


class AtivaGuarnicaoRRDSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarnicaoRRD
        exclude = ["guarnicao", "dataatualizacao"]


class AtivaGuarnicaoTRAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarnicaoTRAV
        exclude = ["guarnicao", "dataatualizacao"]


class ListAtivaGuarnicaoSerializer(serializers.ModelSerializer):
    aits = AtivaGuarnicaoAITSerializer(many=True, source='guarnicaoait_guarnicao')
    rrds = AtivaGuarnicaoRRDSerializer(many=True, source='guarnicaorrd_guarnicao')
    travs = AtivaGuarnicaoTRAVSerializer(many=True, source='guarnicaotrav_guarnicao')

    class Meta:
        model = Guarnicao
        exclude = ["hash"]


class PermutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permuta
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ComandanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policial
        fields = ["id", "matricula", "postograduacao", "nomeguerra"]
        depth = 2


class ListGuarnicaoSerializer(serializers.ModelSerializer):
    comandante = ComandanteSerializer()
    class Meta:
        model = Guarnicao
        fields = ("__all__")


class ListGuarnicaoAITSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarnicaoAIT
        fields = ("__all__")
        depth = 2


class ListGuarnicaoRRDSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarnicaoRRD
        fields = ("__all__")
        depth = 2


class ListGuarnicaoTRAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarnicaoTRAV
        fields = ("__all__")
        depth = 2


class ListPermutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permuta
        fields = ("__all__")
        depth = 2
