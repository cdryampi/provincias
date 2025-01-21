from django.contrib import admin
from .models import ComunidadAutonoma
# Register your models here.
from core.admin.base_img_mixin import filter_logo_queryset

admin.site.register(ComunidadAutonoma)
class ComunidadAutonomaAdmin(admin.ModelAdmin):
    # Toda esta llorería es por la imagen
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'imagen':
            kwargs['queryset'] = filter_logo_queryset('ComunidadAutonoma', request.resolver_match.kwargs.get('object_id'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)