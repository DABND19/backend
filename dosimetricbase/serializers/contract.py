from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)
from dosimetricbase.models import Contract


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ContractListSerializer(ModelSerializer):
    client = StringRelatedField(
        many=False
    )

    class Meta:
        model = Contract
        fields = '__all__'


class ContractViewSerializer(ModelSerializer):
    class Meta:
        model = Contract
        exclude = ['client']
