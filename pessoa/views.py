from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    PessoaSerializer,
    PessoaEnderecoSerializer
)
from .models import (
    Pessoa,
    PessoaEndereco
)


class PessoaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all Pessoa
            Create Pessoa
        HTTP Verbs:
            GET: pessoa/
            POST: pessoa/
    """
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class PessoaDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a Pessoa
            Update of a Pessoa
            Delete of a Pessoa
        HTTP Verbs:
            GET: pessoa/id/ (id do item solicitado)
            PUT: pessoa/id/ (id do item solicitado)
            DELETE: pessoa/id/ (id do item solicitado)
    """
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PessoaEnderecoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all PessoaEndereco
            Create PessoaEndereco
        HTTP Verbs:
            GET: pessoa/endereco/
            POST: pessoa/endereco/
    """
    queryset = PessoaEndereco.objects.all()
    serializer_class = PessoaEnderecoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class PessoaEnderecoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a PessoaEndereco
            Update of a PessoaEndereco
            Delete of a PessoaEndereco
        HTTP Verbs:
            GET: pessoa/endereco/id/ (id do item solicitado)
            PUT: pessoa/endereco/id/ (id do item solicitado)
            DELETE: pessoa/endereco/id/ (id do item solicitado)
    """
    queryset = PessoaEndereco.objects.all()
    serializer_class = PessoaEnderecoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
