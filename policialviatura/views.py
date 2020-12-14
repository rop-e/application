# from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    FuncaoSerializer,
    PolicialViaturaSerializer,
    ListPolicialViaturaSerializer
)
from .models import (
    Funcao,
    PolicialViatura
)


class FuncaoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all Funcao
            Create Funcao
        HTTP Verbs:
            GET: funcao/
            POST: funcao/
    """
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class FuncaoDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a Funcao
            Update of a Funcao
            Delete of a Funcao
        HTTP Verbs:
            GET: funcao/id/ (id do item solicitado)
            PUT: funcao/id/ (id do item solicitado)
            DELETE: funcao/id/ (id do item solicitado)
    """
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PolicialViaturaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all polices
            Create polices
        HTTP Verbs:
            GET: policialviatura/
            POST: policialviatura/
    """
    queryset = PolicialViatura.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListPolicialViaturaSerializer
        else:
            return PolicialViaturaSerializer


class PolicialViaturaDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a police
            Update of a police
            Delete of a polices
        HTTP Verbs:
            GET: policialviatura/id/ (id do item solicitado)
            PUT: policialviatura/id/ (id do item solicitado)
            DELETE: policialviatura/id/ (id do item solicitado)
    """
    queryset = PolicialViatura.objects.all()
    serializer_class = PolicialViaturaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PolicialViaturaAtivaView(generics.ListAPIView):
    """
        ListAtivaView:
            List policialviatura active
        HTTP Verbs:
            GET: policialviatura/ativa/<id da guarnicao>/
    """
    serializer_class = PolicialViaturaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        guarnicao = self.kwargs['id']
        return PolicialViatura.objects.filter(guarnicao=guarnicao)