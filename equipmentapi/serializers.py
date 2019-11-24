from .models import Equipment
from rest_framework import serializers

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ("id_equipment", "title", "id_state", "id_user")