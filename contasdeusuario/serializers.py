from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Usuario
from core.models import Aplicacao


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label="Matrícula", write_only=True)
    password = serializers.CharField(label="Senha", style={"input_type": "password"}, trim_whitespace=False, write_only=True)
    versao = serializers.CharField(label="Versão", write_only=True)
    token = serializers.CharField(label="Token", read_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        versao = attrs.get("versao")

        if versao:
            aplicacao = Aplicacao.objects.filter(versao=versao, atual=True)

            if not aplicacao:
                msg = f"Atualize a sua aplicação. Versão mais atual: {Aplicacao.objects.filter().last().versao}"
                raise serializers.ValidationError(msg, code="version")
        else:
            msg = f"Atualize a sua aplicação. Versão mais atual: {Aplicacao.objects.filter().last().versao}"
            raise serializers.ValidationError(msg, code="version")


        if username and password:
            user = authenticate(request=self.context.get("request"),
                                username=username, password=password)

            if not user:
                msg = "Não foi possível fazer login com as credenciais fornecidas."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Deve incluir "matrícula" e "senha".'
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("__all__")


class AlterarSenhaSerializer(serializers.Serializer):
    model = Usuario

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
