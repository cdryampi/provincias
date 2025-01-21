from rest_framework import serializers
from .models import ComunidadAutonoma

class ComunidadAutonomaSerializer(serializers.ModelSerializer):
    """
    Serializer de ComunidadAutonoma
    """
    class Meta:
        model = ComunidadAutonoma
        fields = '__all__'