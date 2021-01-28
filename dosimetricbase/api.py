from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.permissions import AllowAny

from dosimetricbase.models import (
    Client,
    Contract
)

from dosimetricbase.serializers import (
    ClientListSerializer,
    ClientDetailSerializer
)


class ClientListAPI(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = [
        AllowAny
    ]


class ClientRetrieveAPI(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    permission_classes = [
        AllowAny
    ]


class ContractListAPI(ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = 
