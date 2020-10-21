from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    LocalRecebedorSerializer,
    AgenteRecebedorSerializer
)
from .models import (
    LocalRecebedor,
    AgenteRecebedor
)


class LocalRecebedorListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all local
            Create local
        HTTP Verbs:
            GET: localrecebedor/
            POST: localrecebedor/
    """
    queryset = LocalRecebedor.objects.all()
    serializer_class = LocalRecebedorSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class LocalRecebedorDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a local
            Update of a local
            Delete of a local
        HTTP Verbs:
            GET: localrecebedor/id/ (id do item solicitado)
            PUT: localrecebedor/id/ (id do item solicitado)
            DELETE: localrecebedor/id/ (id do item solicitado)
    """
    queryset = LocalRecebedor.objects.all()
    serializer_class = LocalRecebedorSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class AgenteRecebedorListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all agents
            Create agent
        HTTP Verbs:
            GET: localrecebedor/agenterecebedor/
            POST: localrecebedor/agenterecebedor/
    """
    queryset = AgenteRecebedor.objects.all()
    serializer_class = AgenteRecebedorSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class AgenteRecebedorDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a agents
            Update of a agent
            Delete of a agent
        HTTP Verbs:
            GET: localrecebedor/agenterecebedor/id/ (id do item solicitado)
            PUT: localrecebedor/agenterecebedor/id/ (id do item solicitado)
            DELETE: localrecebedor/agenterecebedor/id/ (id do item solicitado)
    """
    queryset = AgenteRecebedor.objects.all()
    serializer_class = AgenteRecebedorSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
