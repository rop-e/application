# from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    CalibreSerializer,
    UnidadeMedidaSerializer,
    FabricanteArmaSerializer,
    MunicaoAcessorioSerializer,
    VeiculoAcessorioSerializer,
    DocumentoSerializer,
    DocAcessorioSerializer,
    TiposDiversosSerializer,
    DiversosAcessorioSerializer,
    ArmaSerializer,
    TipoArmaSerializer,
    ArmaAcessorioSerializer,
    TipoDrogaSerializer,
    ArmazenamentoDrogaSerializer,
    DrogaAcessorioSerializer,
    ListArmaAcessorioSerializer,
    ListDiversosAcessorioSerializer,
    ListDocAcessorioSerializer,
    ListDrogaAcessorioSerializer,
    ListMunicaoAcessorioSerializer,
    ListVeiculoAcessorioSerializer,
    AcessoriosOcorrenciaSerializer
)

from .models import (
    Calibre,
    UnidadeMedida,
    FabricanteArma,
    MunicaoAcessorio,
    VeiculoAcessorio,
    TipoDoc,
    DocAcessorio,
    TiposDiversos,
    DiversosAcessorio,
    Arma,
    TipoArma,
    ArmaAcessorio,
    TipoDroga,
    ArmazenamentoDroga,
    DrogaAcessorio,
    AcessoriosOcorrencia
)


class AcessoriosOcorrenciaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all calibres
            Create calibres
        HTTP Verbs:
            GET: calibre/
            POST: calibre/
    """
    queryset = AcessoriosOcorrencia.objects.all()
    serializer_class = AcessoriosOcorrenciaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class AcessoriosOcorrenciaDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a calibres
            Update of a calibres
            Delete of a calibres
        HTTP Verbs:
            GET: calibre/id/(id do item solicitado)
            PUT: calibre/id/(id do item solicitado)
            DELETE: calibre/id/(id do item solicitado)
    """
    queryset = AcessoriosOcorrencia.objects.all()
    serializer_class = AcessoriosOcorrenciaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CalibreListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all calibres
            Create calibres
        HTTP Verbs:
            GET: calibre/
            POST: calibre/
    """
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CalibreDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a calibres
            Update of a calibres
            Delete of a calibres
        HTTP Verbs:
            GET: calibre/id/(id do item solicitado)
            PUT: calibre/id/(id do item solicitado)
            DELETE: calibre/id/(id do item solicitado)
    """
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UnidadeMedidaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all UnidadeMedida
            Create UnidadeMedida
        HTTP Verbs:
            GET: unidademedida/
            POST: unidademedida/
    """
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class UnidadeMedidaDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a UnidadeMedida
            Update of a UnidadeMedida
            Delete of a UnidadeMedida
        HTTP Verbs:
            GET: unidademedida/id/(id do item solicitado)
            PUT: unidademedida/id/(id do item solicitado)
            DELETE: unidademedida/id/(id do item solicitado)
    """
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class FabricanteArmaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all fabricantearma
            Create fabricantearma
        HTTP Verbs:
            GET: calibre/
            POST: calibre/
    """
    queryset = FabricanteArma.objects.all()
    serializer_class = FabricanteArmaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class FabricanteArmaDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a fabricantearma
            Update of a fabricantearma
            Delete of a fabricantearma
        HTTP Verbs:
            GET: fabricantearma/id/(id do item solicitado)
            PUT: fabricantearma/id/(id do item solicitado)
            DELETE: fabricantearma/id/(id do item solicitado)
    """
    queryset = FabricanteArma.objects.all()
    serializer_class = FabricanteArmaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class MunicaoAcessorioListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ammunition
            Create ammunition
        HTTP Verbs:
            GET: municaoacessorio/
            POST: municaoacessorio/
    """
    queryset = MunicaoAcessorio.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListMunicaoAcessorioSerializer
        else:
            return MunicaoAcessorioSerializer


class MunicaoAcessorioDetailsUpdateDeleteView(
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
    queryset = MunicaoAcessorio.objects.all()
    serializer_class = MunicaoAcessorioSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TipoArmaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all weapon
            Create weapon
        HTTP Verbs:
            GET: tipoarma/
            POST: tipoarma/
    """
    queryset = TipoArma.objects.all()
    serializer_class = TipoArmaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TipoArmaDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a weapon
            Update of a weapon
            Delete of a weapon
        HTTP Verbs:
            GET: tipoarma/id/(id do item solicitado)
            PUT: tipoarma/id/(id do item solicitado)
            DELETE: tipoarma/id/(id do item solicitado)
    """
    queryset = TipoArma.objects.all()
    serializer_class = TipoArmaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class VeiculoAcessorioListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all seized vehicle
            Create seized vehicle
        HTTP Verbs:
            GET: veiculoacessorio/
            POST: veiculoacessorio/
    """
    queryset = VeiculoAcessorio.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListVeiculoAcessorioSerializer
        else:
            return VeiculoAcessorioSerializer


class VeiculoAcessorioDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a seized vehicle
            Update of a seized vehicle
            Delete of a seized vehicle
        HTTP Verbs:
            GET: veiculoacessorio/id/ (id do item solicitado)
            PUT: veiculoacessorio/id/ (id do item solicitado)
            DELETE: veiculoacessorio/id/ (id do item solicitado)
    """
    queryset = VeiculoAcessorio.objects.all()
    serializer_class = VeiculoAcessorioSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TipoDocListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all TipoDoc
            Create TipoDoc
        HTTP Verbs:
            GET: tipodoc/
            POST: tipodoc/
    """
    queryset = TipoDoc.objects.all()
    serializer_class = DocumentoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TipoDocDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a TipoDoc
            Update of a TipoDoc
            Delete of a TipoDoc
        HTTP Verbs:
            GET: tipodoc/id/ (id do item solicitado)
            PUT: tipodoc/id/ (id do item solicitado)
            DELETE: tipodoc/id/ (id do item solicitado)
    """
    queryset = TipoDoc.objects.all()
    serializer_class = DocumentoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class DocAcessorioListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all doc
            Create doc
        HTTP Verbs:
            GET: docacessorio/
            POST: docacessorio/
    """
    queryset = DocAcessorio.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListDocAcessorioSerializer
        else:
            return DocAcessorioSerializer


class DocAcessorioDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a doc
            Update of a doc
            Delete of a doc
        HTTP Verbs:
            GET: docacessorio/id/ (id do item solicitado)
            PUT: docacessorio/id/ (id do item solicitado)
            DELETE: docacessorio/id/ (id do item solicitado)
    """
    queryset = DocAcessorio.objects.all()
    serializer_class = DocAcessorioSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TiposDiversosListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all TiposDiversos
            Create TiposDiversos
        HTTP Verbs:
            GET: tiposdiversos/
            POST: tiposdiversos/
    """
    queryset = TiposDiversos.objects.all()
    serializer_class = TiposDiversosSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TiposDiversosDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a TiposDiversos
            Update of a TiposDiversos
            Delete of a TiposDiversos
        HTTP Verbs:
            GET: tiposdiversos/id/ (id do item solicitado)
            PUT: tiposdiversos/id/ (id do item solicitado)
            DELETE: tiposdiversos/id/ (id do item solicitado)
    """
    queryset = TiposDiversos.objects.all()
    serializer_class = TiposDiversosSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class DiversosAcessorioListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all others
            Create others
        HTTP Verbs:
            GET: diversosacessorio/
            POST: diversosacessorio/
    """
    queryset = DiversosAcessorio.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListDiversosAcessorioSerializer
        else:
            return DiversosAcessorioSerializer


class DiversosAcessorioDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a others
            Update of a others
            Delete of a others
        HTTP Verbs:
            GET: diversosacessorio/id/ (id do item solicitado)
            PUT: diversosacessorio/id/ (id do item solicitado)
            DELETE: diversosacessorio/id/ (id do item solicitado)
    """
    queryset = DiversosAcessorio.objects.all()
    serializer_class = DiversosAcessorioSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ArmaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all weapons
            Create weapon
        HTTP Verbs:
            GET: arma/
            POST: arma/
    """
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ArmaDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a weapons
            Update of a weapon
            Delete of a weapon
        HTTP Verbs:
            GET: arma/id/ (id do item solicitado)
            PUT: arma/id/ (id do item solicitado)
            DELETE: arma/id/ (id do item solicitado)
    """
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ArmaAcessorioListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all weapons
            Create weapon
        HTTP Verbs:
            GET: armaacessorio/
            POST: armaacessorio/
    """
    queryset = ArmaAcessorio.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListArmaAcessorioSerializer
        else:
            return ArmaAcessorioSerializer


class ArmaAcessorioDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a weapons
            Update of a weapon
            Delete of a weapon
        HTTP Verbs:
            GET: armaacessorio/id/ (id do item solicitado)
            PUT: armaacessorio/id/ (id do item solicitado)
            DELETE: armaacessorio/id/ (id do item solicitado)
    """
    queryset = ArmaAcessorio.objects.all()
    serializer_class = ArmaAcessorioSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TipoDrogaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all TipoDroga
            Create TipoDroga
        HTTP Verbs:
            GET: tipodroga/
            POST: tipodroga/
    """
    queryset = TipoDroga.objects.all()
    serializer_class = TipoDrogaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TipoDrogaDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a TipoDroga
            Update of a TipoDroga
            Delete of a TipoDroga
        HTTP Verbs:
            GET: tipodroga/id/ (id do item solicitado)
            PUT: tipodroga/id/ (id do item solicitado)
            DELETE: tipodroga/id/ (id do item solicitado)
    """
    queryset = TipoDroga.objects.all()
    serializer_class = TipoDrogaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ArmazenamentoDrogaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all ArmazenamentoDroga
            Create ArmazenamentoDroga
        HTTP Verbs:
            GET: armazenamentodroga/
            POST: armazenamentodroga/
    """
    queryset = ArmazenamentoDroga.objects.all()
    serializer_class = ArmazenamentoDrogaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ArmazenamentoDrogaDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a ArmazenamentoDroga
            Update of a ArmazenamentoDroga
            Delete of a ArmazenamentoDroga
        HTTP Verbs:
            GET: armazenamentodroga/id/ (id do item solicitado)
            PUT: armazenamentodroga/id/ (id do item solicitado)
            DELETE: armazenamentodroga/id/ (id do item solicitado)
    """
    queryset = ArmazenamentoDroga.objects.all()
    serializer_class = ArmazenamentoDrogaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class DrogaAcessorioListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all drugs
            Create drug
        HTTP Verbs:
            GET: drogaacessorio/
            POST: drogaacessorio/
    """
    queryset = DrogaAcessorio.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListDrogaAcessorioSerializer
        else:
            return DrogaAcessorioSerializer


class DrogaAcessorioDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a drugs
            Update of a drug
            Delete of a drug
        HTTP Verbs:
            GET: drogaacessorio/id/ (id do item solicitado)
            PUT: drogaacessorio/id/ (id do item solicitado)
            DELETE: drogaacessorio/id/ (id do item solicitado)
    """
    queryset = DrogaAcessorio.objects.all()
    serializer_class = DrogaAcessorioSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
