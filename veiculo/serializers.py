from rest_framework import serializers
from .models import (
    CategoriaVeiculo,
    MarcaVeiculo,
    Veiculo
)


class CategoriaVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaVeiculo
        fields = ("__all__")


class MarcaVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaVeiculo
        fields = ("__all__")


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ListVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )
        depth = 1
