from django.db import models
from multimedia_manager.models import MediaFile 
# Create your models here.
class ComunidadAutonoma(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre",
        help_text="Nombre de la Comunidad Autónoma"
    )
    descripcion = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descripción",
        help_text="Descripción de la Comunidad Autónoma"
    )
    codigo = models.CharField(
        max_length=2,
        unique=True,
        verbose_name="Código",
        help_text="Código de la Comunidad Autónoma"
    )
    imagen = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text="Imagen de la Comunidad Autónoma"
    )
    class Meta:
        verbose_name_plural = "Comunidades Autónomas"
        verbose_name = "Comunidad Autónoma"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre