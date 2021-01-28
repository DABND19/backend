from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from rest_framework.permissions import AllowAny

from dosimetricbase.models import Contract

from dosimetricbase.serializers import (
    ContractSerializer,
    ContractListSerializer
)


class ContractAPI(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [
        AllowAny
    ]
