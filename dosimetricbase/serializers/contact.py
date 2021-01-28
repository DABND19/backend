from rest_framework.serializers import ModelSerializer
from dosimetricbase.models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactViewSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'fullname', 'phone', 'email']
