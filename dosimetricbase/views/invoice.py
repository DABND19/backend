from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from dosimetricbase.models import Invoice
from dosimetricbase.serializers import InvoiceListSerializer


class InvoiceListView(ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceListSerializer
    permission_classes = [
        AllowAny
    ]
