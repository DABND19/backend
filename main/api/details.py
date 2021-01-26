from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny # Для тестирования

from main.serializers.details import (
    OrganisationDetailSerializer
)

from main.models import (
    Organisation
)

class OrganisationDetailView(GenericViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationDetailSerializer
    permissions = [
        AllowAny
    ]
