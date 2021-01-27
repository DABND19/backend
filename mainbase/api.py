from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import AllowAny

from mainbase.models import (
    Counterparty,
    ActualAddress,
    LegalContact
)

from mainbase.serializers.views import (
    CounterpartyListSerializer,
    CounterpartyDetailSerializer
)

from mainbase.serializers.models import (
    ActualAddressSerializer,
    LegalContactSerializer
)


class CounterpartyListAPI(ListCreateAPIView):
    queryset = Counterparty.objects.all()
    serializer_class = CounterpartyListSerializer
    permission_classes = [
        AllowAny
    ]


class CounterpartyRetrieveAPI(RetrieveUpdateDestroyAPIView):
    queryset = Counterparty.objects.all()
    serializer_class = CounterpartyDetailSerializer
    permission_classes = [
        AllowAny
    ]


class ActualAddressAPI(ModelViewSet):
    queryset = ActualAddress.objects.all()
    serializer_class = ActualAddressSerializer
    permission_classes = [
        AllowAny
    ]


class LegalContactAPI(ModelViewSet):
    queryset = LegalContact.objects.all()
    serializer_class = LegalContactSerializer
    permission_classes = [
        AllowAny
    ]
