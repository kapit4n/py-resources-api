from rest_framework import serializers
from .models import Resource

class ResourceSerialzer(serializers.ModelSerializer):
  class Meta:
    model = Resource
    fields = ('name', )