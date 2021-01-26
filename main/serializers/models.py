from rest_framework.serializers import (
    ModelSerializer
)

from main.models import (
    Organisation,
    Address,
    LegalAddress,
    Contact,
    LegalContact
)


class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class LegalAddressSerializer(ModelSerializer):
    detail = AddressSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = LegalAddress
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class LegalContactSerializer(ModelSerializer):
    detail = ContactSerializer(
        many=False,
        read_only=True
    )
    
    class Meta:
        model = LegalContact
        fields = '__all__'
