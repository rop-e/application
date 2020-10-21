# from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    EstadosSerializer,
    MunicipiosSerializer,
    EnderecoSerializer
)
from .models import (
    Estados,
    Municipios,
    Endereco
)


class EstadosListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all Estados
            Create Estados
        HTTP Verbs:
            GET: estados/
            POST: estados/
    """
    queryset = Estados.objects.all()
    serializer_class = EstadosSerializer

    # Autenticacao base
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # Permissoes base
    #   - IsAuthenticated define que precisa esta logado no sistema
    #   - IsAdmin define que precisa ser o Admin logado no sistema
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class EstadosDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a Estados
            Update of a Estados
            Delete of a Estados
        HTTP Verbs:
            GET: endereco/id/ (id do item solicitado)
            PUT: endereco/id/ (id do item solicitado)
            DELETE: endereco/id/ (id do item solicitado)
    """
    queryset = Estados.objects.all()
    serializer_class = EstadosSerializer

    # Autenticacao base
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # Permissoes base
    #   - IsAuthenticated define que precisa esta logado no sistema
    #   - IsAdmin define que precisa ser o Admin logado no sistema
    permission_classes = [IsAuthenticated]


class MunicipiosListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all Municipios
            Create Municipios
        HTTP Verbs:
            GET: municipios/
            POST: municipios/
    """
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSerializer

    # Autenticacao base
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # Permissoes base
    #   - IsAuthenticated define que precisa esta logado no sistema
    #   - IsAdmin define que precisa ser o Admin logado no sistema
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class MunicipiosDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a Municipios
            Update of a Municipios
            Delete of a Municipios
        HTTP Verbs:
            GET: municipios/id/ (id do item solicitado)
            PUT: municipios/id/ (id do item solicitado)
            DELETE: municipios/id/ (id do item solicitado)
    """
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSerializer

    # Autenticacao base
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # Permissoes base
    #   - IsAuthenticated define que precisa esta logado no sistema
    #   - IsAdmin define que precisa ser o Admin logado no sistema
    permission_classes = [IsAuthenticated]


class EnderecoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all address
            Create address
        HTTP Verbs:
            GET: endereco/
            POST: endereco/
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    # Autenticacao base
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # Permissoes base
    #   - IsAuthenticated define que precisa esta logado no sistema
    #   - IsAdmin define que precisa ser o Admin logado no sistema
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class EnderecoDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a address
            Update of a address
            Delete of a address
        HTTP Verbs:
            GET: endereco/id/ (id do item solicitado)
            PUT: endereco/id/ (id do item solicitado)
            DELETE: endereco/id/ (id do item solicitado)
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    # Autenticacao base
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # Permissoes base
    #   - IsAuthenticated define que precisa esta logado no sistema
    #   - IsAdmin define que precisa ser o Admin logado no sistema
    permission_classes = [IsAuthenticated]
