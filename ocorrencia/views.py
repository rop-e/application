from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    OcorrenciaSerializer,
    InfracaoSerializer,
    ListOcorrenciaSerializer,
    TipoOcorrenciaSerializer
)
from .models import (
    Ocorrencia,
    Infracao,
    TipoOcorrencia
)


class OcorrenciaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all occurrence
            Create occurrence
        HTTP Verbs:
            GET: ocorrencia/
            POST: ocorrencia/
    """
    queryset = Ocorrencia.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListOcorrenciaSerializer
        else:
            return OcorrenciaSerializer


class OcorrenciaDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a occurrence
            Update of a occurrence
            Delete of a occurrence
        HTTP Verbs:
            GET: ocorrencia/id/ (id do item solicitado)
            PUT: ocorrencia/id/ (id do item solicitado)
            DELETE: ocorrencia/id/ (id do item solicitado)
    """
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TipoInfracaoListCreateView(generics.ListCreateAPIView):
    queryset = Infracao.objects.all()
    serializer_class = InfracaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TipoOcorrenciaListCreateView(generics.ListCreateAPIView):
    queryset = TipoOcorrencia.objects.all()
    serializer_class = TipoOcorrenciaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
