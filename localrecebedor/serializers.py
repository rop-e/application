from rest_framework import serializers
from .models import (
    LocalRecebedor,
    AgenteRecebedor
)


class LocalRecebedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalRecebedor
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class AgenteRecebedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenteRecebedor
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )
