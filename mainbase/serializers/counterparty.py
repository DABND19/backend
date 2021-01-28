from rest_framework.serializers import ModelSerializer
from mainbase.models import Counterparty

from .actualaddress import ActualAddressViewSerializer
from .legalcontact import LegalContactViewSerializer


class CounterpartySerializer(ModelSerializer):
    class Meta:
        model = Counterparty
        fields = '__all__'


class CounterpartyListSerializer(ModelSerializer):
    class Meta:
        model = Counterparty
        fields = '__all__'


class CounterpartyDetailSerializer(ModelSerializer):
    legal_contacts = LegalContactViewSerializer(
        many=True,
        read_only=True
    )
    actual_addresses = ActualAddressViewSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Counterparty
        fields = '__all__'
