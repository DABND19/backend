from rest_framework.serializers import ModelSerializer
from mainbase.models import LegalContact


class LegalContactSerializer(ModelSerializer):
    class Meta:
        model = LegalContact
        fields = '__all__'


class LegalContactViewSerializer(ModelSerializer):
    class Meta:
        model = LegalContact
        fields = ['id', 'fullname', 'phone', 'email']
