from rest_framework import serializers
from .models import (
    PolicialViatura,
    Funcao
)


class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = ("__all__")


class PolicialViaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicialViatura
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ListPolicialViaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicialViatura
        fields = ("__all__")
        depth = 2
