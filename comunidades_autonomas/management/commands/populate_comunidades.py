from django.core.management.base import BaseCommand
from django.core.files import File
from comunidades_autonomas.models import ComunidadAutonoma
from multimedia_manager.models import MediaFile
import os

class Command(BaseCommand):
    help = 'Poblar las comunidades autónomas de España en la base de datos con imágenes'

    def handle(self, *args, **kwargs):
        # Ruta base donde se encuentran las imágenes
        base_path = "media/sample/comunidades/"
        
        # Datos de las comunidades autónomas con imágenes
        comunidades = [
            {"nombre": "Andalucía", "codigo": "AN", "imagen": "andalucia.jpg"},
            {"nombre": "Aragón", "codigo": "AR", "imagen": "aragon.jpg"},
            {"nombre": "Asturias", "codigo": "AS", "imagen": "asturias.jpg"},
            {"nombre": "Cantabria", "codigo": "CB", "imagen": "cantabria.jpg"},
            {"nombre": "Castilla y León", "codigo": "CL", "imagen": "castillayleon.jpg"},
            {"nombre": "Castilla-La Mancha", "codigo": "CM", "imagen": "castillalamancha.jpg"},
            {"nombre": "Cataluña", "codigo": "CT", "imagen": "cataluna.jpg"},
            {"nombre": "Extremadura", "codigo": "EX", "imagen": "extremadura.jpg"},
            {"nombre": "Galicia", "codigo": "GA", "imagen": "galicia.jpg"},
            {"nombre": "Madrid", "codigo": "MD", "imagen": "madrid.jpg"},
            {"nombre": "Murcia", "codigo": "MC", "imagen": "murcia.jpg"},
            {"nombre": "Navarra", "codigo": "NC", "imagen": "navarra.jpg"},
            {"nombre": "País Vasco", "codigo": "PV", "imagen": "paisvasco.jpg"},
            {"nombre": "La Rioja", "codigo": "RI", "imagen": "larioja.jpg"},
            {"nombre": "Valencia", "codigo": "VC", "imagen": "valencia.jpg"},
            {"nombre": "Ceuta", "codigo": "CE", "imagen": "ceuta.jpg"},
            {"nombre": "Melilla", "codigo": "ML", "imagen": "melilla.jpg"},
        ]
            # eliminar los modelos de comunidad
        ComunidadAutonoma.objects.all().delete()
        
        for comunidad in comunidades:
            # Ruta completa del archivo de imagen
            image_path = os.path.join(base_path, comunidad["imagen"])

            # Verificar que el archivo existe
            if not os.path.exists(image_path):
                self.stdout.write(self.style.ERROR(f'Archivo no encontrado: {image_path}'))
                continue

            # Crear o recuperar el archivo multimedia
            with open(image_path, 'rb') as image_file:
                django_file = File(image_file)
                media_file, _ = MediaFile.objects.get_or_create(
                    file=comunidad["imagen"],
                    defaults={
                        "title": comunidad["nombre"]
                    }
                )
                # Guardar el archivo para simular la subida
                media_file.file.save(comunidad["imagen"], django_file, save=True)

            # Crear o actualizar la comunidad autónoma
            obj, created = ComunidadAutonoma.objects.update_or_create(
                codigo=comunidad["codigo"],
                defaults={
                    "nombre": comunidad["nombre"],
                    "imagen": media_file,
                }
            )

            # Mostrar el estado en la consola
            if created:
                self.stdout.write(self.style.SUCCESS(f'Comunidad creada: {comunidad["nombre"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Comunidad actualizada: {comunidad["nombre"]}'))

        self.stdout.write(self.style.SUCCESS('¡Todas las comunidades han sido procesadas con imágenes!'))
