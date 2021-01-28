from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from dosimetricbase.models import TransmittedDocument

from .quarter import QuarterShortSerializer


class TransmittedDocumentSerializer(ModelSerializer):
    class Meta:
        model = TransmittedDocument
        fields = '__all__'


class TransmittedDocumentViewSerializer(ModelSerializer):
    quarter = QuarterShortSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = TransmittedDocument
        exclude = ['client']
