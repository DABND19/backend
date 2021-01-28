from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from dosimetricbase.models import Client

from dosimetricbase.serializers import ClientSerializer


class ClientAPI(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        AllowAny
    ]
