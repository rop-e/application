# from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    CategoriaVeiculoSerializer,
    MarcaVeiculoSerializer,
    VeiculoSerializer,
    ListVeiculoSerializer
)
from .models import (
    CategoriaVeiculo,
    MarcaVeiculo,
    Veiculo
)


class CategoriaVeiculoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all CATEGORIA VEICULO
            Create CATEGORIA VEICULO
        HTTP Verbs:
            GET: veiculo/categoria/
            POST: veiculo/categoria/
    """
    queryset = CategoriaVeiculo.objects.all()
    serializer_class = CategoriaVeiculoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CategoriaVeiculoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a CATEGORIA VEICULO
            Update of a CATEGORIA VEICULO
            Delete of a CATEGORIA VEICULO
        HTTP Verbs:
            GET: veiculo/categoria/id/ (id do item solicitado)
            PUT: veiculo/categoria/id/ (id do item solicitado)
            DELETE: veiculo/categoria/id/ (id do item solicitado)
    """
    queryset = CategoriaVeiculo.objects.all()
    serializer_class = CategoriaVeiculoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class MarcaVeiculoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all MARCA VEICULO
            Create MARCA VEICULO
        HTTP Verbs:
            GET: veiculo/marca/
            POST: veiculo/marca/
    """
    queryset = MarcaVeiculo.objects.all()
    serializer_class = MarcaVeiculoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class MarcaVeiculoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a MARCA VEICULO
            Update of a MARCA VEICULO
            Delete of a MARCA VEICULO
        HTTP Verbs:
            GET: veiculo/marca/id/ (id do item solicitado)
            PUT: veiculo/marca/id/ (id do item solicitado)
            DELETE: veiculo/marca/id/ (id do item solicitado)
    """
    queryset = MarcaVeiculo.objects.all()
    serializer_class = MarcaVeiculoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class VeiculoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all vehicles
            Create vehicles
        HTTP Verbs:
            GET: veiculo/
            POST: veiculo/
    """
    queryset = Veiculo.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListVeiculoSerializer
        else:
            return VeiculoSerializer


class VeiculoDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a vehicle
            Update of a vehicle
            Delete of a vehicles
        HTTP Verbs:
            GET: veiculo/id/ (id do item solicitado)
            PUT: veiculo/id/ (id do item solicitado)
            DELETE: veiculo/id/ (id do item solicitado)
    """
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
