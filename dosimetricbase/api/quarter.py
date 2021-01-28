from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from dosimetricbase.models import Quarter
from dosimetricbase.serializers import QuarterSerializer


class QuarterAPI(ModelViewSet):
    queryset = Quarter.objects.all()
    serializer_class = QuarterSerializer
    permission_classes = [
        AllowAny
    ]
