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
    TipoOcorrenciaSerializer,
    ListOcorrenciaFilterSerializer
)
from .models import (
    Ocorrencia,
    Infracao,
    TipoOcorrencia
)
from datetime import date


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


class OcorrenciaDateFilterListView(generics.ListAPIView):
    serializer_class = ListOcorrenciaFilterSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        diaI = self.kwargs["diaI"]
        mesI = self.kwargs["mesI"]
        anoI = self.kwargs["anoI"]
        diaF = self.kwargs["diaF"]
        mesF = self.kwargs["mesF"]
        anoF = self.kwargs["anoF"]
        datainicial = date(anoI, mesI, diaI)
        datafinal = date(anoF, mesF, diaF)

        return Ocorrencia.objects.filter(dataocorrencia__range=(datainicial, datafinal))


class OcorrenciaEnvolvidosFilterListView(generics.ListAPIView):
    serializer_class = ListOcorrenciaFilterSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        envolvido = self.kwargs["envolvido"]
        return Ocorrencia.objects.filter(envolvido__pessoa__nome__icontains=envolvido)
