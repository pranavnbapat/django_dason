from rest_framework import serializers
from .models import PDF2Text, FakerModel
from django.urls import reverse


class PDF2TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF2Text
        fields = '__all__'


class FakerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakerModel
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation[
            'contact_no_link'] = f'<a href="{reverse("backend:record-click", args=[instance.contact_no])}" class="contact_no_link" data-contact_no="{instance.contact_no}">{instance.contact_no}</a>'
        return representation

