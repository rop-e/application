from rest_framework import serializers
from .models import (
    TipoAcidente,
    CondicaoVia,
    CondicaoSinalizacao,
    TracadoVia,
    CondicaoMeteorologica,
    Pavimentacao,
    RAT,
    RATObjetos,
    RATVeiculos,
    RATVeiculoEnvolvidos
)
from envolvido.models import Envolvido
from acessoriosocorrencia.models import Veiculo


class TipoAcidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAcidente
        fields = ("__all__")


class CondicaoViaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicaoVia
        fields = ("__all__")


class CondicaoSinalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicaoSinalizacao
        fields = ("__all__")


class TracadoViaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TracadoVia
        fields = ("__all__")


class CondicaoMeteorologicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicaoMeteorologica
        fields = ("__all__")


class PavimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pavimentacao
        fields = ("__all__")


class RATSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAT
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class RATObjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RATObjetos
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class RATVeiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RATVeiculos
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class RATVeiculoEnvolvidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RATVeiculoEnvolvidos
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ListRATSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAT
        fields = ("__all__")
        depth = 2


class ListRATObjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RATObjetos
        fields = ("__all__")
        depth = 2


class ListRATVeiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RATVeiculos
        fields = ("__all__")
        depth = 2


class ListRATVeiculoEnvolvidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RATVeiculoEnvolvidos
        fields = ("__all__")
        depth = 2


class ObjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RATObjetos
        exclude = ["datacriacao", "dataatualizacao", "rat"]


class ListVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        exclude = ["datacriacao", "dataatualizacao"]


class VeiculosSerializer(serializers.ModelSerializer):
    veiculo = ListVeiculoSerializer()

    class Meta:
        model = RATVeiculos
        exclude = ["datacriacao", "dataatualizacao", "rat"]


class EnvolvidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envolvido
        exclude = ["datacriacao", "dataatualizacao", "rat", "ocorrencia"]


class ListRATsGuarnicaoFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAT
        exclude = ["guarnicao", "status_previa", "datacriacao", "dataatualizacao", "hash"]


class ListApreensoesRatSerializer(serializers.ModelSerializer):
    envolvidos = EnvolvidoSerializer(many=True, source='envolvido_rat')
    veiculos = VeiculosSerializer(many=True, source='ratveiculos_rat')
    objetos = ObjetosSerializer(many=True, source='ratobjetos_rat')

    class Meta:
        model = RAT
        fields = ["id", "envolvidos", "veiculos", "objetos"]
