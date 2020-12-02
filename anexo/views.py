from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    AnexoSerializer
)
from .models import (
    Anexo
)


class AnexoListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all Anexo
            Create Anexo
        HTTP Verbs:
            GET: Anexo/
            POST: Anexo/
    """
    queryset = Anexo.objects.all()
    serializer_class = AnexoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class AnexoDetailsUpdateDeleteView(
        generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a Anexo
            Update of a Anexo
            Delete of a Anexo
        HTTP Verbs:
            GET: Anexo/id/ (id do item solicitado)
            PUT: Anexo/id/ (id do item solicitado)
            DELETE: Anexo/id/ (id do item solicitado)
    """
    queryset = Anexo.objects.all()
    serializer_class = AnexoSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
