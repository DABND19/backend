from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from dosimetricbase.models import ActualAddress

from dosimetricbase.serializers import ActualAddressSerializer

class ActualAddressAPI(ModelViewSet):
    queryset = ActualAddress.objects.all()
    serializer_class = ActualAddressSerializer
    permission_classes = [
        AllowAny
    ]
