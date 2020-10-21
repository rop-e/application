from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import ObservacaoSerializer
from .models import Observacao


class ObservacaoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all note
            Create note
        HTTP Verbs:
            GET: observacao/
            POST: observacao/
    """
    queryset = Observacao.objects.all()
    serializer_class = ObservacaoSerializer

    # Autenticacao base
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # Permissoes base
    #   - IsAuthenticated define que precisa esta logado no sistema
    #   - IsAdmin define que precisa ser o Admin logado no sistema
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ObservacaoDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a note
            Update of a note
            Delete of a note
        HTTP Verbs:
            GET: observacao/id/ (id do item solicitado)
            PUT: observacao/id/ (id do item solicitado)
            DELETE: observacao/id/ (id do item solicitado)
    """
    queryset = Observacao.objects.all()
    serializer_class = ObservacaoSerializer

    # Autenticacao base
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # Permissoes base
    #   - IsAuthenticated define que precisa esta logado no sistema
    #   - IsAdmin define que precisa ser o Admin logado no sistema
    permission_classes = [IsAuthenticated]
