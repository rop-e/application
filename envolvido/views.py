from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    TipoEnvolvimentoSerializer,
    EnvolvidoSerializer,
    TipoLesaoSerializer,
    ListLesaoSerializer,
    LesaoSerializer,
    ListEnvolvidoSerializer
)
from .models import (
    TipoEnvolvimento,
    Envolvido,
    Lesao,
    TipoLesao
)


class TipoEnvolvimentoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all TipoEnvolvimento
            Create TipoEnvolvimento
        HTTP Verbs:
            GET: tipoenvolvimento/
            POST: tipoenvolvimento/
    """
    queryset = TipoEnvolvimento.objects.all()
    serializer_class = TipoEnvolvimentoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TipoEnvolvimentoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a TipoEnvolvimento
            Update of a TipoEnvolvimento
            Delete of a TipoEnvolvimento
        HTTP Verbs:
            GET: tipoenvolvimento/id/ (id do item solicitado)
            PUT: tipoenvolvimento/id/ (id do item solicitado)
            DELETE: tipoenvolvimento/id/ (id do item solicitado)
    """
    queryset = TipoEnvolvimento.objects.all()
    serializer_class = TipoEnvolvimentoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class EnvolvidoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all involved
            Create involved
        HTTP Verbs:
            GET: envolvido/
            POST: envolvido/
    """
    queryset = Envolvido.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListEnvolvidoSerializer
        else:
            return EnvolvidoSerializer


class EnvolvidoDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a involved
            Update of a involved
            Delete of a involved
        HTTP Verbs:
            GET: envolvido/id/ (id do item solicitado)
            PUT: envolvido/id/ (id do item solicitado)
            DELETE: envolvido/id/ (id do item solicitado)
    """
    queryset = Envolvido.objects.all()
    serializer_class = EnvolvidoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TipoLesaoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all TipoLesao
            Create TipoLesao
        HTTP Verbs:
            GET: tipolesao/
            POST: tipolesao/
    """
    queryset = TipoLesao.objects.all()
    serializer_class = TipoLesaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TipoLesaoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a TipoLesao
            Update of a TipoLesao
            Delete of a TipoLesao
        HTTP Verbs:
            GET: tipolesao/id/ (id do item solicitado)
            PUT: tipolesao/id/ (id do item solicitado)
            DELETE: tipolesao/id/ (id do item solicitado)
    """
    queryset = TipoLesao.objects.all()
    serializer_class = TipoLesaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class LesaoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all Lesao
            Create Lesao
        HTTP Verbs:
            GET: lesao/
            POST: lesao/
    """
    queryset = Lesao.objects.all()
    serializer_class = LesaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListLesaoSerializer
        else:
            return LesaoSerializer


class LesaoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a Lesao
            Update of a Lesao
            Delete of a Lesao
        HTTP Verbs:
            GET: lesao/id/ (id do item solicitado)
            PUT: lesao/id/ (id do item solicitado)
            DELETE: lesao/id/ (id do item solicitado)
    """
    queryset = Lesao.objects.all()
    serializer_class = LesaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
