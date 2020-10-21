from rest_framework import generics
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from .serializers import ViaturaSerializer
from .models import Viatura


class ViaturaListCreateView(generics.ListCreateAPIView):
    """
        ListCreateView:
            List all police car
            Create police car
        HTTP Verbs:
            GET: viatura/
            POST: viatura/
    """
    queryset = Viatura.objects.all()
    serializer_class = ViaturaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ViaturaDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView:
            Details of a police car
            Update of a police car
            Delete of a police cars
        HTTP Verbs:
            GET: viatura/id/ (id do item solicitado)
            PUT: viatura/id/ (id do item solicitado)
            DELETE: viatura/id/ (id do item solicitado)
    """
    queryset = Viatura.objects.all()
    serializer_class = ViaturaSerializer

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
