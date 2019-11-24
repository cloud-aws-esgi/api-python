from .models import State
from rest_framework import serializers

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ("id_state", "title")