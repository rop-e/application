from rest_framework import serializers
from .models import (
    Pessoa,
    PessoaEndereco
)


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class PessoaEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaEndereco
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )
