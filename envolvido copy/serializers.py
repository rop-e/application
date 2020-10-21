from rest_framework import serializers
from .models import (
    Envolvido,
    TipoEnvolvimento,
    TipoLesao,
    Lesao
)


class TipoEnvolvimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEnvolvimento
        fields = ("__all__")


class EnvolvidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envolvido
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class TipoLesaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLesao
        fields = ("__all__")


class LesaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesao
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ListEnvolvidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envolvido
        fields = ("__all__")
        depth = 2
