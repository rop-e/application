from rest_framework import serializers
from .models import Observacao


class ObservacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observacao
        fields = (
            'id',
            'observacao',
        )
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )
