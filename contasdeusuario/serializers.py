from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("__all__")


class AlterarSenhaSerializer(serializers.Serializer):
    model = Usuario

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
