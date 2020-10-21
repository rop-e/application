from rest_framework import serializers
from .models import (
    Policial,
    PostoGraduacao,
    Cargo,
    TipoSanguineo
)
from contasdeusuario.models import Usuario


class TipoSanguineoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSanguineo
        fields = ("__all__")


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ("__all__")


class PostoGraduacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostoGraduacao
        fields = ("__all__")


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("__all__")


class PolicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policial
        fields = ("__all__")
        read_only_fields = (
            "datacriacao",
            "dataatualizacao",
        )


class ListPolicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policial
        fields = ("__all__")
        depth = 2
