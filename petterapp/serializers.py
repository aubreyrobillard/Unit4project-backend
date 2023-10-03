from .models import Petter
from django.contrib.auth.models import User, Group
from rest_framework import serializers


# Petter Serializer

class PetterSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Petter
        fields = '__all__'

    