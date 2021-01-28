from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from dosimetricbase.models import Contract, Invoice
from dosimetricbase.serializers import InvoiceSerializer


class InvoiceAPI(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [
        AllowAny
    ]
