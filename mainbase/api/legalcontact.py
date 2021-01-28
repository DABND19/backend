from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny

from mainbase.models import LegalContact

from mainbase.serializers import LegalContactSerializer


class LegalContactAPI(ModelViewSet):
    queryset = LegalContact.objects.all()
    serializer_class = LegalContactSerializer
    permission_classes = [
        AllowAny
    ]
