from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import ComunidadAutonomaViewSet

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de Comunidades Autónomas",
        default_version='v1',
        description="API para listar y gestionar las comunidades autónomas de España",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="soporte@api.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

# Configuración de las rutas de la API
router = DefaultRouter()
router.register(r'', ComunidadAutonomaViewSet, basename='comunidad-autonoma')

urlpatterns = [
    path('lista_comunidades/', include(router.urls)),  # Endpoints de la API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
]
