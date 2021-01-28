from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny

from mainbase.models import ActualAddress

from mainbase.serializers import ActualAddressSerializer


class ActualAddressAPI(ModelViewSet):
    queryset = ActualAddress.objects.all()
    serializer_class = ActualAddressSerializer
    permission_classes = [
        AllowAny
    ]
