from rest_framework import serializers
from .models import (
    MunicaoAcessorio,
    VeiculoAcessorio,
    DocAcessorio,
    DiversosAcessorio,
    Arma,
    ArmaAcessorio,
    DrogaAcessorio,
    AcessoriosOcorrencia,
    Calibre,
    TipoDoc,
    TiposDiversos,
    FabricanteArma,
    TipoArma,
    TipoDroga,
    ArmazenamentoDroga,
    UnidadeMedida
)


class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeMedida
        fields = ("__all__")


class AcessoriosOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcessoriosOcorrencia
        fields = ("__all__")


class CalibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibre
        fields = ("__all__")


class MunicaoAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicaoAcessorio
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class VeiculoAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeiculoAcessorio
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDoc
        fields = ("__all__")


class DocAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocAcessorio
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class TiposDiversosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposDiversos
        fields = ("__all__")


class DiversosAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiversosAcessorio
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class TipoArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoArma
        fields = ("__all__")


class FabricanteArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricanteArma
        fields = ("__all__")


class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ArmaAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmaAcessorio
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class TipoDrogaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDroga
        fields = ("__all__")


class ArmazenamentoDrogaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmazenamentoDroga
        fields = ("__all__")


class DrogaAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrogaAcessorio
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ListMunicaoAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicaoAcessorio
        fields = ("__all__")
        depth = 2


class ListVeiculoAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeiculoAcessorio
        fields = ("__all__")
        depth = 2


class ListDocAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocAcessorio
        fields = ("__all__")
        depth = 2


class ListDiversosAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiversosAcessorio
        fields = ("__all__")
        depth = 2


class ListArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = ("__all__")
        depth = 2


class ListArmaAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmaAcessorio
        fields = ("__all__")
        depth = 2


class ListDrogaAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrogaAcessorio
        fields = ("__all__")
        depth = 2
