from rest_framework import serializers
from .models import Viatura


class ViaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viatura
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )
