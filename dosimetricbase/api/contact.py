from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from dosimetricbase.models import Contact

from dosimetricbase.serializers import ContactSerializer


class ContactAPI(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [
        AllowAny
    ]
