from rest_framework import serializers
from multimedia_manager.serializers import MediaFileSerializer
from .models import ComunidadAutonoma

class ComunidadAutonomaSerializer(serializers.ModelSerializer):
    """
    Serializer de ComunidadAutonoma
    """
    imagen = MediaFileSerializer()
    class Meta:
        model = ComunidadAutonoma
        fields = ['id', 'nombre', 'descripcion', 'codigo', 'imagen']