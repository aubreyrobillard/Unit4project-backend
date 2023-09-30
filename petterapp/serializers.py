from .models import Petter
from rest_framework import serializers


# Petter Serializer

class PetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petter
        fields = '__all__'
    