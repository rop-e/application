from rest_framework import serializers
from .models import (
    Batalhao,
    BatalhaoMunicipios
)
from endereco.serializers import MunicipiosSerializer


class BatalhaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batalhao
        fields = ("__all__")


class BatalhaoMunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatalhaoMunicipios
        fields = ("__all__")


class ListBatalhaoMunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatalhaoMunicipios
        fields = ("__all__")
        depth = 2
