from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from dosimetricbase.models import TransmittedDocument
from dosimetricbase.serializers import TransmittedDocumentSerializer


class TransmittedDocumentAPI(ModelViewSet):
    queryset = TransmittedDocument.objects.all()
    serializer_class = TransmittedDocumentSerializer
    permission_classes = [
        AllowAny
    ]
