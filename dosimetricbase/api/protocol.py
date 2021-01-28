from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from dosimetricbase.models import Protocol
from dosimetricbase.serializers import ProtocolSerializer


class ProtocolAPI(ModelViewSet):
    queryset = Protocol.objects.all()
    serializer_class = ProtocolSerializer
    permission_classes = [
        AllowAny
    ]
