from rest_framework import serializers
from .models import PDF2Text


class PDF2TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF2Text
        fields = '__all__'
