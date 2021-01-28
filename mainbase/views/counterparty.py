from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from rest_framework.permissions import AllowAny

from mainbase.models import Counterparty

from mainbase.serializers import (
    CounterpartyDetailSerializer,
    CounterpartyListSerializer
)


class CounterpartyListView(ListAPIView):
    queryset = Counterparty.objects.all()
    serializer_class = CounterpartyListSerializer
    permission_classes = [
        AllowAny
    ]


class CounterpartyDetailView(RetrieveAPIView):
    queryset = Counterparty.objects.all()
    serializer_class = CounterpartyDetailSerializer
    permission_classes = [
        AllowAny
    ]
