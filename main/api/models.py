from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny # Для тестирования

from main.models import (
    Organisation,
    Address,
    LegalAddress,
    Contact,
    LegalContact
)

from main.serializers.models import (
    OrganisationSerializer,
    AddressSerializer,
    LegalAddressSerializer,
    ContactSerializer,
    LegalContactSerializer
)

class OrganisationAPI(ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [
        AllowAny
    ]


class AddressAPI(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [
        AllowAny
    ]


class LegalAddressAPI(ModelViewSet):
    queryset = LegalAddress.objects.all()
    serializer_class = LegalAddressSerializer
    permission_classes = [
        AllowAny
    ]


class ContactAPI(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [
        AllowAny
    ]


class LegalContactAPI(ModelViewSet):
    queryset = LegalContact.objects.all()
    serializer_class = LegalContactSerializer
    permission_classes = [
        AllowAny
    ]
