from django.shortcuts import render
from rest_framework import generics
from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework import viewsets

# Create your views here.
class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer