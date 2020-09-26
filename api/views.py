from django.shortcuts import render
from rest_framework.response import Response
from api import models,serializers
from rest_framework.generics import(
    ListAPIView,
    RetrieveAPIView
)
class Home(ListAPIView):
    queryset=models.Entity.objects.all()
    serializer_class=serializers.Entity_serializer
class Details(RetrieveAPIView):
    queryset=models.Entity.objects.all()
    serializer_class=serializers.Entity_serializer   