from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from dosimetricbase.models import Client

from dosimetricbase.serializers import (
    ClientListSerializer,
    ClientDetailSerializer
)


class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = [
        AllowAny
    ]


class ClientDetailView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    permission_classes = [
        AllowAny
    ]
