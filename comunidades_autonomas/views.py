from rest_framework import viewsets
from .models import ComunidadAutonoma
from .serializers import ComunidadAutonomaSerializer
# Create your views here.

class ComunidadAutonomaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Comunidades Autónomas to be viewed or edited.
    """
    queryset = ComunidadAutonoma.objects.all()
    serializer_class = ComunidadAutonomaSerializer