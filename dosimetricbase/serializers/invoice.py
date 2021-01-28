from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from dosimetricbase.models import Invoice

from .quarter import QuarterShortSerializer


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceListSerializer(ModelSerializer):
    quarter = QuarterShortSerializer(
        many=False,
        read_only=True
    )
    client = StringRelatedField(
        many=False,
        read_only=True
    )

    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceViewSerializer(ModelSerializer):
    quarter = QuarterShortSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = Invoice
        exclude = ['client']
