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


class ListEnvolvidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envolvido
        fields = ("__all__")
        depth = 2


class EnvolvidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envolvido
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ListTipoLesaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLesao
        fields = ("tipo",)


class TipoLesaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLesao
        fields = ("__all__")


class ListLesaoSerializer(serializers.ModelSerializer):
    tipolesao = ListTipoLesaoSerializer()

    class Meta:
        model = Lesao
        exclude = ["dataatualizacao", "datacriacao"]


class LesaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesao
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )
