from rest_framework import serializers
from .models import (
    Endereco,
    Municipios,
    Estados
)


class EstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        fields = ("__all__")


class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipios
        fields = ("__all__")


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )
