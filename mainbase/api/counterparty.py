from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.permissions import AllowAny

from mainbase.models import Counterparty

from mainbase.serializers import (
    CounterpartyDetailSerializer,
    CounterpartyListSerializer
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
