# from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    TipoServicoSerializer,
    ModalidadedePoliciamentoSerializer,
    CompanhiaSerializer,
    GuarnicaoSerializer,
    ListGuarnicaoSerializer,
    GuarnicaoAITSerializer,
    GuarnicaoRRDSerializer,
    GuarnicaoTRAVSerializer,
    PermutaSerializer
)
from .models import (
    TipoServico,
    ModalidadedePoliciamento,
    Companhia,
    Guarnicao,
    GuarnicaoAIT,
    GuarnicaoRRD,
    GuarnicaoTRAV,
    Permuta
)


class TipoServicoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all TipoServico
            Create TipoServico
        HTTP Verbs:
            GET: tiposervico/
            POST: tiposervico/
    """
    queryset = TipoServico.objects.all()
    serializer_class = TipoServicoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TipoServicoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a TipoServico
            Update of a TipoServico
            Delete of a TipoServico
        HTTP Verbs:
            GET: tiposervico/id/ (id do item solicitado)
            PUT: tiposervico/id/ (id do item solicitado)
            DELETE: tiposervico/id/ (id do item solicitado)
    """
    queryset = TipoServico.objects.all()
    serializer_class = TipoServicoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ModalidadedePoliciamentoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ModalidadedePoliciamento
            Create ModalidadedePoliciamento
        HTTP Verbs:
            GET: modalidadepoliciamento/
            POST: modalidadepoliciamento/
    """
    queryset = ModalidadedePoliciamento.objects.all()
    serializer_class = ModalidadedePoliciamentoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ModalidadedePoliciamentoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ModalidadedePoliciamento
            Update of a ModalidadedePoliciamento
            Delete of a ModalidadedePoliciamento
        HTTP Verbs:
            GET: modalidadepoliciamento/id/ (id do item solicitado)
            PUT: modalidadepoliciamento/id/ (id do item solicitado)
            DELETE: modalidadepoliciamento/id/ (id do item solicitado)
    """
    queryset = ModalidadedePoliciamento.objects.all()
    serializer_class = ModalidadedePoliciamentoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CompanhiaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all Companhia
            Create Companhia
        HTTP Verbs:
            GET: companhia/
            POST: companhia/
    """
    queryset = Companhia.objects.all()
    serializer_class = CompanhiaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CompanhiaDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a Companhia
            Update of a Companhia
            Delete of a Companhia
        HTTP Verbs:
            GET: companhia/id/ (id do item solicitado)
            PUT: companhia/id/ (id do item solicitado)
            DELETE: companhia/id/ (id do item solicitado)
    """
    queryset = Companhia.objects.all()
    serializer_class = CompanhiaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class GuarnicaoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all garrison
            Create garrison
        HTTP Verbs:
            GET: guarnicao/
            POST: guarnicao/
    """
    queryset = Guarnicao.objects.all()
    serializer_class = GuarnicaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class GuarnicaoDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a garrison
            Update of a garrison
            Delete of a garrison
        HTTP Verbs:
            GET: guarnicao/id/ (id do item solicitado)
            PUT: guarnicao/id/ (id do item solicitado)
            DELETE: guarnicao/id/ (id do item solicitado)
    """
    queryset = Guarnicao.objects.all()
    serializer_class = GuarnicaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class GuarnicaoAITListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all GuarnicaoAIT
            Create GuarnicaoAIT
        HTTP Verbs:
            GET: guarnicao/ait/
            POST: guarnicao/ait/
    """
    queryset = GuarnicaoAIT.objects.all()
    serializer_class = GuarnicaoAITSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class GuarnicaoAITDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a GuarnicaoAIT
            Update of a GuarnicaoAIT
            Delete of a GuarnicaoAIT
        HTTP Verbs:
            GET: guarnicao/ait/id/ (id do item solicitado)
            PUT: guarnicao/ait/id/ (id do item solicitado)
            DELETE: guarnicao/ait/id/ (id do item solicitado)
    """
    queryset = GuarnicaoAIT.objects.all()
    serializer_class = GuarnicaoAITSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class GuarnicaoRRDListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all GuarnicaoRRD
            Create GuarnicaoRRD
        HTTP Verbs:
            GET: guarnicao/rrd/
            POST: guarnicao/rrd/
    """
    queryset = GuarnicaoRRD.objects.all()
    serializer_class = GuarnicaoRRDSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class GuarnicaoRRDDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a GuarnicaoRRD
            Update of a GuarnicaoRRD
            Delete of a GuarnicaoRRD
        HTTP Verbs:
            GET: guarnicao/rrd/id/ (id do item solicitado)
            PUT: guarnicao/rrd/id/ (id do item solicitado)
            DELETE: guarnicao/rrd/id/ (id do item solicitado)
    """
    queryset = GuarnicaoRRD.objects.all()
    serializer_class = GuarnicaoRRDSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class GuarnicaoTRAVListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all GuarnicaoTRAV
            Create GuarnicaoTRAV
        HTTP Verbs:
            GET: guarnicao/trav/
            POST: guarnicao/trav/
    """
    queryset = GuarnicaoTRAV.objects.all()
    serializer_class = GuarnicaoTRAVSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class GuarnicaoTRAVDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a GuarnicaoTRAV
            Update of a GuarnicaoTRAV
            Delete of a GuarnicaoTRAV
        HTTP Verbs:
            GET: guarnicao/trav/id/ (id do item solicitado)
            PUT: guarnicao/trav/id/ (id do item solicitado)
            DELETE: guarnicao/trav/id/ (id do item solicitado)
    """
    queryset = GuarnicaoTRAV.objects.all()
    serializer_class = GuarnicaoTRAVSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PermutaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all Permuta
            Create Permuta
        HTTP Verbs:
            GET: guarnicao/permuta/
            POST: guarnicao/permuta/
    """
    queryset = Permuta.objects.all()
    serializer_class = PermutaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class PermutaDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a Permuta
            Update of a Permuta
            Delete of a Permuta
        HTTP Verbs:
            GET: guarnicao/permuta/id/ (id do item solicitado)
            PUT: guarnicao/permuta/id/ (id do item solicitado)
            DELETE: guarnicao/permuta/id/ (id do item solicitado)
    """
    queryset = Permuta.objects.all()
    serializer_class = PermutaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class GuarnicaoAtivaView(generics.ListAPIView):
    """
        ListAtivaView:
            List garrison active
        HTTP Verbs:
            GET: guarnicao/ativa/<id do comandante>/
    """
    serializer_class = GuarnicaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        comandante = self.kwargs['id']
        return Guarnicao.objects.filter(comandante=comandante, datafechamento__isnull=True)


class GuarnicaoAtivasView(generics.ListAPIView):
    """
        ListAtivaView:
            List garrisons active
        HTTP Verbs:
            GET: guarnicao/ativas/
    """
    serializer_class = ListGuarnicaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Guarnicao.objects.filter(datafechamento__isnull=True)
