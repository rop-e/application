from rest_framework import serializers
from .models import (
    OPOTipoEvento,
    OPO,
    OPORelatorio,
    OPOComandantesCIA
)


class OPOTipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPOTipoEvento
        fields = ("__all__")


class OPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPO
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class OPORelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPORelatorio
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ListOPORelatorioSerializer(serializers.ModelSerializer):
    dataexecucao = serializers.DateTimeField(format="%d/%m/%Y às %H:%M")
    datafinalizacao = serializers.DateTimeField(format="%d/%m/%Y às %H:%M")

    class Meta:
        model = OPORelatorio
        fields = ("__all__")
        depth = 2


class ListOPOComandantesCIASerializer(serializers.ModelSerializer):
    class Meta:
        model = OPOComandantesCIA
        fields = ("__all__")
        depth = 2
