from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    OPOTipoEventoSerializer,
    OPOSerializer,
    OPORelatorioSerializer
)
from .models import (
    OPOTipoEvento,
    OPO,
    OPORelatorio
)


class OPOTipoEventoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all OPOTipoEvento
            Create OPOTipoEvento
        HTTP Verbs:
            GET: opo/tipoevento/
            POST: opo/tipoevento/
    """
    queryset = OPOTipoEvento.objects.all()
    serializer_class = OPOTipoEventoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class OPOTipoEventoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a OPOTipoEvento
            Update of a OPOTipoEvento
            Delete of a OPOTipoEvento
        HTTP Verbs:
            GET: opo/tipoevento/id/ (id do item solicitado)
            PUT: opo/tipoevento/id/ (id do item solicitado)
            DELETE: opo/tipoevento/id/ (id do item solicitado)
    """
    queryset = OPOTipoEvento.objects.all()
    serializer_class = OPOTipoEventoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class OPOListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all OPO
            Create OPO
        HTTP Verbs:
            GET: opo/
            POST: opo/
    """
    queryset = OPO.objects.all()
    serializer_class = OPOSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class OPODetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a OPO
            Update of a OPO
            Delete of a OPO
        HTTP Verbs:
            GET: opo/id/ (id do item solicitado)
            PUT: opo/id/ (id do item solicitado)
            DELETE: opo/id/ (id do item solicitado)
    """
    queryset = OPO.objects.all()
    serializer_class = OPOSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class OPORelatorioListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all OPORelatorio
            Create OPORelatorio
        HTTP Verbs:
            GET: opo/relatorio/
            POST: opo/relatorio/
    """
    queryset = OPORelatorio.objects.all()
    serializer_class = OPORelatorioSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class OPORelatorioDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a OPORelatorio
            Update of a OPORelatorio
            Delete of a OPORelatorio
        HTTP Verbs:
            GET: opo/relatorio/id/ (id do item solicitado)
            PUT: opo/relatorio/id/ (id do item solicitado)
            DELETE: opo/relatorio/id/ (id do item solicitado)
    """
    queryset = OPORelatorio.objects.all()
    serializer_class = OPORelatorioSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
