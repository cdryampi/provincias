from django.contrib import admin
from multimedia_manager.models import MediaFile
# Register your models here.
@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    pass