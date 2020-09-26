from rest_framework import serializers
from api import models
class Entity_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Entity
        fields="__all__"