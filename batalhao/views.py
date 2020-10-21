# from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    BatalhaoSerializer,
    BatalhaoMunicipiosSerializer,
    ListBatalhaoMunicipiosSerializer
)
from .models import (
    Batalhao,
    BatalhaoMunicipios
)


class BatalhaoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all Batalhao
            Create Batalhao
        HTTP Verbs:
            GET: batalhao/
            POST: batalhao/
    """
    queryset = Batalhao.objects.all()
    serializer_class = BatalhaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BatalhaoDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a Batalhao
            Update of a Batalhao
            Delete of a Batalhao
        HTTP Verbs:
            GET: batalhao/id/ (id do item solicitado)
            PUT: batalhao/id/ (id do item solicitado)
            DELETE: batalhao/id/ (id do item solicitado)
    """
    queryset = Batalhao.objects.all()
    serializer_class = BatalhaoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class BatalhaoMunicipiosListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all BatalhaoMunicipios
            Create BatalhaoMunicipios
        HTTP Verbs:
            GET: batalhaomunicipios/
            POST: batalhaomunicipios/
    """
    queryset = BatalhaoMunicipios.objects.all()

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
        
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListBatalhaoMunicipiosSerializer
        else:
            return BatalhaoMunicipiosSerializer


class BatalhaoMunicipiosDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a BatalhaoMunicipios
            Update of a BatalhaoMunicipios
            Delete of a BatalhaoMunicipios
        HTTP Verbs:
            GET: batalhaomunicipios/id/ (id do item solicitado)
            PUT: batalhaomunicipios/id/ (id do item solicitado)
            DELETE: batalhaomunicipios/id/ (id do item solicitado)
    """
    queryset = BatalhaoMunicipios.objects.all()
    serializer_class = BatalhaoMunicipiosSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
