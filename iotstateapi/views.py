from django.shortcuts import render
from rest_framework import generics
from .models import State
from .serializers import StateSerializer
from rest_framework import viewsets

# Create your views here.
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer