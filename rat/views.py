from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    TipoAcidenteSerializer,
    CondicaoViaSerializer,
    CondicaoSinalizacaoSerializer,
    TracadoViaSerializer,
    CondicaoMeteorologicaSerializer,
    PavimentacaoSerializer,
    RATSerializer,
    RATObjetosSerializer,
    RATVeiculosSerializer,
    RATVeiculoEnvolvidosSerializer
)
from .models import (
    TipoAcidente,
    CondicaoVia,
    CondicaoSinalizacao,
    TracadoVia,
    CondicaoMeteorologica,
    Pavimentacao,
    RAT,
    RATObjetos,
    RATVeiculos,
    RATVeiculoEnvolvidos
)


class TipoAcidenteListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ammunition
            Create ammunition
        HTTP Verbs:
            GET: municaoacessorio/
            POST: municaoacessorio/
    """

    queryset = TipoAcidente.objects.all()
    serializer_class = TipoAcidenteSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TipoAcidenteDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ammunition
            Update of a ammunition
            Delete of a ammunition
        HTTP Verbs:
            GET: municaoacessorio/id/(id do item solicitado)
            PUT: municaoacessorio/id/(id do item solicitado)
            DELETE: municaoacessorio/id/(id do item solicitado)
    """
    queryset = TipoAcidente.objects.all()
    serializer_class = TipoAcidenteSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CondicaoViaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ammunition
            Create ammunition
        HTTP Verbs:
            GET: municaoacessorio/
            POST: municaoacessorio/
    """
    queryset = CondicaoVia.objects.all()
    serializer_class = CondicaoViaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CondicaoViaDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ammunition
            Update of a ammunition
            Delete of a ammunition
        HTTP Verbs:
            GET: municaoacessorio/id/(id do item solicitado)
            PUT: municaoacessorio/id/(id do item solicitado)
            DELETE: municaoacessorio/id/(id do item solicitado)
    """
    queryset = CondicaoVia.objects.all()
    serializer_class = CondicaoViaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CondicaoSinalizacaoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ammunition
            Create ammunition
        HTTP Verbs:
            GET: municaoacessorio/
            POST: municaoacessorio/
    """
    queryset = CondicaoSinalizacao.objects.all()
    serializer_class = CondicaoSinalizacaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CondicaoSinalizacaoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ammunition
            Update of a ammunition
            Delete of a ammunition
        HTTP Verbs:
            GET: municaoacessorio/id/(id do item solicitado)
            PUT: municaoacessorio/id/(id do item solicitado)
            DELETE: municaoacessorio/id/(id do item solicitado)
    """
    queryset = CondicaoSinalizacao.objects.all()
    serializer_class = CondicaoSinalizacaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TracadoViaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ammunition
            Create ammunition
        HTTP Verbs:
            GET: municaoacessorio/
            POST: municaoacessorio/
    """
    queryset = TracadoVia.objects.all()
    serializer_class = TracadoViaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TracadoViaDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ammunition
            Update of a ammunition
            Delete of a ammunition
        HTTP Verbs:
            GET: municaoacessorio/id/(id do item solicitado)
            PUT: municaoacessorio/id/(id do item solicitado)
            DELETE: municaoacessorio/id/(id do item solicitado)
    """
    queryset = TracadoVia.objects.all()
    serializer_class = TracadoViaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CondicaoMeteorologicaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ammunition
            Create ammunition
        HTTP Verbs:
            GET: municaoacessorio/
            POST: municaoacessorio/
    """
    queryset = CondicaoMeteorologica.objects.all()
    serializer_class = CondicaoMeteorologicaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CondicaoMeteorologicaDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ammunition
            Update of a ammunition
            Delete of a ammunition
        HTTP Verbs:
            GET: municaoacessorio/id/(id do item solicitado)
            PUT: municaoacessorio/id/(id do item solicitado)
            DELETE: municaoacessorio/id/(id do item solicitado)
    """
    queryset = CondicaoMeteorologica.objects.all()
    serializer_class = CondicaoMeteorologicaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PavimentacaoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ammunition
            Create ammunition
        HTTP Verbs:
            GET: municaoacessorio/
            POST: municaoacessorio/
    """
    queryset = Pavimentacao.objects.all()
    serializer_class = PavimentacaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class PavimentacaoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ammunition
            Update of a ammunition
            Delete of a ammunition
        HTTP Verbs:
            GET: municaoacessorio/id/(id do item solicitado)
            PUT: municaoacessorio/id/(id do item solicitado)
            DELETE: municaoacessorio/id/(id do item solicitado)
    """
    queryset = Pavimentacao.objects.all()
    serializer_class = PavimentacaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class RATListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all rat
            Create rat
        HTTP Verbs:
            GET: rat/
            POST: rat/
    """
    queryset = RAT.objects.all()
    serializer_class = RATSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class RATDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a rat
            Update of a rat
            Delete of a rat
        HTTP Verbs:
            GET: rat/id/(id do item solicitado)
            PUT: rat/id/(id do item solicitado)
            DELETE: rat/id/(id do item solicitado)
    """
    queryset = RAT.objects.all()
    serializer_class = RATSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class RATObjetosListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ratobjetos
            Create ratobjetos
        HTTP Verbs:
            GET: rat/objetos/
            POST: rat/objetos/
    """
    queryset = RATObjetos.objects.all()
    serializer_class = RATObjetosSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class RATObjetosDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ratobjetos
            Update of a ratobjetos
            Delete of a ratobjetos
        HTTP Verbs:
            GET: rat/objetos/id/(id do item solicitado)
            PUT: rat/objetos/id/(id do item solicitado)
            DELETE: rat/objetos/id/(id do item solicitado)
    """
    queryset = RATObjetos.objects.all()
    serializer_class = RATObjetosSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class RATVeiculosListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ratveiculos
            Create ratveiculos
        HTTP Verbs:
            GET: rat/veiculos/
            POST: rat/veiculos/
    """
    queryset = RATVeiculos.objects.all()
    serializer_class = RATVeiculosSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class RATVeiculosDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ratveiculos
            Update of a ratveiculos
            Delete of a ratveiculos
        HTTP Verbs:
            GET: rat/veiculos/id/(id do item solicitado)
            PUT: rat/veiculos/id/(id do item solicitado)
            DELETE: rat/veiculos/id/(id do item solicitado)
    """
    queryset = RATVeiculos.objects.all()
    serializer_class = RATVeiculosSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class RATVeiculoEnvolvidosListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ratveiculoenvolvidos
            Create ratveiculoenvolvidos
        HTTP Verbs:
            GET: rat/veiculoenvolvidos/
            POST: rat/veiculoenvolvidos/
    """
    queryset = RATVeiculoEnvolvidos.objects.all()
    serializer_class = RATVeiculoEnvolvidosSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class RATVeiculoEnvolvidosDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ratveiculoenvolvidos
            Update of a ratveiculoenvolvidos
            Delete of a ratveiculoenvolvidos
        HTTP Verbs:
            GET: rat/veiculoenvolvidos/id/(id do item solicitado)
            PUT: rat/veiculoenvolvidos/id/(id do item solicitado)
            DELETE: rat/veiculoenvolvidos/id/(id do item solicitado)
    """
    queryset = RATVeiculoEnvolvidos.objects.all()
    serializer_class = RATVeiculoEnvolvidosSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
