from rest_framework.serializers import ModelSerializer

from dosimetricbase.models import Protocol

from .quarter import QuarterShortSerializer


class ProtocolSerializer(ModelSerializer):
    class Meta:
        model = Protocol
        fields = '__all__'


class ProtocolViewSerializer(ModelSerializer):
    quarter = QuarterShortSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = Protocol
        exclude = ['client']
