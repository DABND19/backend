from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from dosimetricbase.models import Contract
from dosimetricbase.serializers import ContractListSerializer


class ContractListView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer
    permission_classes = [
        AllowAny
    ]
