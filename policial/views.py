# from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    PolicialSerializer,
    ListPolicialSerializer
)
from .models import Policial


class PolicialListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all polices
            Create polices
        HTTP Verbs:
            GET: policial/
            POST: policial/
    """
    queryset = Policial.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListPolicialSerializer
        else:
            return PolicialSerializer


class PolicialDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a police
            Update of a police
            Delete of a polices
        HTTP Verbs:
            GET: policial/id/ (id do item solicitado)
            PUT: policial/id/ (id do item solicitado)
            DELETE: policial/id/ (id do item solicitado)
    """
    queryset = Policial.objects.all()
    serializer_class = PolicialSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
