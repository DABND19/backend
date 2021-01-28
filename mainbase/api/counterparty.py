from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from mainbase.models import Counterparty
from mainbase.serializers import CounterpartySerializer


class CounterpartyAPI(ModelViewSet):
    queryset = Counterparty.objects.all()
    serializer_class = CounterpartySerializer
    permission_classes = [
        AllowAny
    ]
