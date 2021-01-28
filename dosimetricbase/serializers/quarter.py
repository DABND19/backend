from rest_framework.serializers import ModelSerializer

from dosimetricbase.models import Quarter


class QuarterSerializer(ModelSerializer):
    class Meta:
        model = Quarter
        fields = '__all__'


class QuarterShortSerializer(ModelSerializer):
    class Meta:
        model = Quarter
        fields = ['year', 'number']
