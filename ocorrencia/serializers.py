from rest_framework import serializers
from .models import (
    Ocorrencia,
    TipoOcorrencia,
    Infracao,
    ObservacaoOcorrencia,
    Orgao
)
from guarnicao.models import Guarnicao
from policial.models import Policial
from endereco.models import (
    Endereco,
    Municipios,
    Estados
)

class TipoOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOcorrencia
        fields = ("__all__")


class InfracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infracao
        fields = ("__all__")


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ("__all__")
        read_only_fields = (
            'datacriacao',
            'dataatualizacao',
        )


class ObservacaoOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservacaoOcorrencia
        fields = ("__all__")


class ListOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ("__all__")
        depth = 2


class ListObservacaoOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservacaoOcorrencia
        fields = ("__all__")
        depth = 2


class PolicialFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policial
        fields = ["nomeguerra"]


class GuarnicaoFilterSerializer(serializers.ModelSerializer):
    comandante = PolicialFilterSerializer()
    class Meta:
        model = Guarnicao
        fields = ["comandante"]


class OrgaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgao
        fields = ("__all__")


class ListOcorrenciaFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        exclude = ["status_previa", "datacriacao", "dataatualizacao", "hash"]
        depth = 2


class ListOcorrenciasGuarnicaoFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        exclude = ["guarnicao", "status_previa", "datacriacao", "dataatualizacao", "hash"]


from acessoriosocorrencia.models import (
    AcessoriosOcorrencia,
    ArmaAcessorio,
    Arma,
    DrogaAcessorio,
    MunicaoAcessorio,
    VeiculoAcessorio,
    DocAcessorio,
    Veiculo,
    DiversosAcessorio
)
from envolvido.models import Envolvido

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        exclude = ["datacriacao", "dataatualizacao"]


class ArmaAcessorioSerializer(serializers.ModelSerializer):
    arma = ArmaSerializer()

    class Meta:
        model = ArmaAcessorio
        exclude = ["datacriacao", "dataatualizacao", "acessoriosocorrencia"]


class DrogaAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrogaAcessorio
        exclude = ["datacriacao", "dataatualizacao", "acessoriosocorrencia"]


class MunicaoAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicaoAcessorio
        exclude = ["datacriacao", "dataatualizacao", "acessoriosocorrencia"]


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        exclude = ["datacriacao", "dataatualizacao"]


class VeiculoAcessorioSerializer(serializers.ModelSerializer):
    veiculo = VeiculoSerializer()

    class Meta:
        model = VeiculoAcessorio
        exclude = ["datacriacao", "dataatualizacao", "acessoriosocorrencia"]


class DocAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocAcessorio
        exclude = ["datacriacao", "dataatualizacao", "acessoriosocorrencia"]


class DiversosAcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiversosAcessorio
        exclude = ["datacriacao", "dataatualizacao", "acessoriosocorrencia"]


class AcessoriosOcorrenciaSerializer(serializers.ModelSerializer):
    armas = ArmaAcessorioSerializer(many=True, source='armaacessorio_acessoriosocorrencia')
    drogas = DrogaAcessorioSerializer(many=True, source='drogaacessorio_acessoriosocorrencia')
    municoes = MunicaoAcessorioSerializer(many=True, source='municaoacessorio_acessoriosocorrencia')
    veiculos = VeiculoAcessorioSerializer(many=True, source='veiculoacessorio_acessoriosocorrencia')
    documentos = DocAcessorioSerializer(many=True, source='docacessorio_acessoriosocorrencia')
    objetos = DiversosAcessorioSerializer(many=True, source='diversosacessorio_acessoriosocorrencia')

    class Meta:
        model = AcessoriosOcorrencia
        fields = ["armas", "drogas", "municoes", "veiculos", "documentos", "objetos"]


class EnvolvidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envolvido
        exclude = ["datacriacao", "dataatualizacao", "ocorrencia", "rat"]


class ListApreensoesOcorrenciaSerializer(serializers.ModelSerializer):
    envolvidos = EnvolvidoSerializer(many=True, source='envolvido_ocorrencia')
    apreensoes = AcessoriosOcorrenciaSerializer(many=True, source='acessoriosocorrencia_ocorrencia')

    class Meta:
        model = Ocorrencia
        fields = ["id", "envolvidos", "apreensoes"]
