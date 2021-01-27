from rest_framework.serializers import (
    ModelSerializer
)

from mainbase.models import (
    Counterparty,
    LegalContact,
    ActualAddress
)


class LegalContactSerializer(ModelSerializer):
    class Meta:
        model = LegalContact
        fields = '__all__'


class ActualAddressSerializer(ModelSerializer):
    class Meta:
        model = ActualAddress
        fields = '__all__'
