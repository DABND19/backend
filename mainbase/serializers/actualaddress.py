from rest_framework.serializers import ModelSerializer

from mainbase.models import ActualAddress


class ActualAddressSerializer(ModelSerializer):
    class Meta:
        model = ActualAddress
        fields = '__all__'


class ActualAddressViewSerializer(ModelSerializer):
    class Meta:
        model = ActualAddress
        fields = ['id', 'full']
