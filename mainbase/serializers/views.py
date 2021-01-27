from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from mainbase.models import (
    ActualAddress,
    Counterparty,
    LegalContact
)


class LegalContactViewSerializer(ModelSerializer):
    class Meta:
        model = LegalContact
        fields = ['id', 'fullname', 'phone', 'email']


class ActualAddressViewSerializer(ModelSerializer):
    class Meta:
        model = ActualAddress
        fields = ['id', 'full']


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
