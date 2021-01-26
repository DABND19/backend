from rest_framework.serializers import (
    ModelSerializer
)

from main.models import (
    Organisation
)

from main.serializers.models import (
    LegalAddressSerializer,
    LegalContactSerializer
)


class OrganisationDetailSerializer(ModelSerializer):
    legal_addresses = LegalAddressSerializer(
        many=True,
        read_only=True
    )
    legal_contacts = LegalContactSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Organisation
        fields = '__all__'
