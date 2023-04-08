from rest_framework import serializers
from .models import PDF2Text, FakerModel


class PDF2TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF2Text
        fields = '__all__'


class FakerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakerModel
        fields = '__all__'

