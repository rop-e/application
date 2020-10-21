from rest_framework import serializers
from .models import Anexo


class AnexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anexo
        fields = ("__all__")
        read_only_fields = (
            "datacriacao",
            "dataatualizacao",
        )


class ListAnexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anexo
        fields = ("__all__")
        depth = 2
