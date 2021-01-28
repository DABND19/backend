from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from dosimetricbase.models import Client

from mainbase.serializers import CounterpartyListSerializer
from .actualaddress import ActualAddressViewSerializer
from .contact import ContactViewSerializer
from .contract import ContractViewSerializer
from .invoice import InvoiceViewSerializer
from .protocol import ProtocolViewSerializer
from .transmitteddocument import TransmittedDocumentViewSerializer


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientListSerializer(ModelSerializer):
    organisation = CounterpartyListSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = Client
        fields = '__all__'


class ClientDetailSerializer(ModelSerializer):
    actual_addresses = ActualAddressViewSerializer(
        many=True,
        read_only=True
    )
    contacts = ContactViewSerializer(
        many=True,
        read_only=True
    )
    contracts = ContractViewSerializer(
        many=True,
        read_only=True
    )
    protocols = ProtocolViewSerializer(
        many=True,
        read_only=True
    )
    invoices = InvoiceViewSerializer(
        many=True,
        read_only=True
    )
    transmitted_documents = TransmittedDocumentViewSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Client
        fields = '__all__'
