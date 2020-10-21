# from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import ProcedimentoOcorrenciaSerializer
from .models import ProcedimentoOcorrencia


class ProcedimentoOcorrenciaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all procedures
            Create procedure
        HTTP Verbs:
            GET: procedimentoocorrencia/
            POST: procedimentoocorrencia/
    """
    queryset = ProcedimentoOcorrencia.objects.all()
    serializer_class = ProcedimentoOcorrenciaSerializer

    # Autenticacao base
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # Permissoes base
    #   - IsAuthenticated define que precisa esta logado no sistema
    #   - IsAdmin define que precisa ser o Admin logado no sistema
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ProcedimentoOcorrenciaDetailsUpdateDeleteView(
      generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a procedures
            Update of a procedure
            Delete of a procedure
        HTTP Verbs:
            GET: procedimentoocorrencia/id/ (id do item solicitado)
            PUT: procedimentoocorrencia/id/ (id do item solicitado)
            DELETE: procedimentoocorrencia/id/ (id do item solicitado)
    """
    queryset = ProcedimentoOcorrencia.objects.all()
    serializer_class = ProcedimentoOcorrenciaSerializer

    # Autenticacao base
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # Permissoes base
    #   - IsAuthenticated define que precisa esta logado no sistema
    #   - IsAdmin define que precisa ser o Admin logado no sistema
    permission_classes = [IsAuthenticated]
