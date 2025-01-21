from django.core.management.base import BaseCommand
from django.core.files import File
from comunidades_autonomas.models import ComunidadAutonoma
from multimedia_manager.models import MediaFile
import os

class Command(BaseCommand):
    help = 'Poblar las comunidades autónomas de España en la base de datos con imágenes'

    def handle(self, *args, **kwargs):
        # Ruta base donde se encuentran las imágenes
        base_path = "comunidades_autonomas/management/sample_data/comunidades/"
        
        # Datos de las comunidades autónomas con imágenes
        comunidades = [
            {"nombre": "Andalucía", "codigo": "AN", "imagen": "andalucia.jpg", "descripcion": "Andalucía es una comunidad autónoma española reconocida como nacionalidad histórica por su Estatuto de Autonomía, cuyo territorio se encuentra en el sur de la península ibérica."},
            {"nombre": "Aragón", "codigo": "AR", "imagen": "aragon.jpg", "descripcion": "Aragón es una comunidad autónoma uniprovincial de España, situada en el noreste del país."},
            {"nombre": "Asturias", "codigo": "AS", "imagen": "asturias.jpg", "descripcion": "Asturias es una comunidad autónoma uniprovincial de España, situada en el norte de la península ibérica."},
            {"nombre": "Cantabria", "codigo": "CB", "imagen": "cantabria.jpg", "descripcion": "Cantabria es una comunidad autónoma uniprovincial de España, situada en el norte de la península ibérica."},
            {"nombre": "Castilla y León", "codigo": "CL", "imagen": "castillayleon.jpg", "descripcion": "Castilla y León es una comunidad autónoma española, situada en el noroeste de la península ibérica."},
            {"nombre": "Castilla-La Mancha", "codigo": "CM", "imagen": "castillalamancha.jpg", "descripcion": "Castilla-La Mancha es una comunidad autónoma española situada en el centro de la península ibérica."},
            {"nombre": "Cataluña", "codigo": "CT", "imagen": "cataluna.jpg", "descripcion": "Cataluña es una comunidad autónoma española, considerada nacionalidad histórica, situada al noreste de la península ibérica."},
            {"nombre": "Extremadura", "codigo": "EX", "imagen": "extremadura.jpg", "descripcion": "Extremadura es una comunidad autónoma española situada en el suroeste de la península ibérica."},
            {"nombre": "Galicia", "codigo": "GA", "imagen": "galicia.jpg", "descripcion": "Galicia es una comunidad autónoma española situada en el noroeste de la península ibérica."},
            {"nombre": "Madrid", "codigo": "MD", "imagen": "madrid.jpg", "descripcion": "Madrid es una comunidad autónoma española situada en el centro de la península ibérica."},
            {"nombre": "Murcia", "codigo": "MC", "imagen": "murcia.jpg", "descripcion": "Murcia es una comunidad autónoma española situada en el sureste de la península ibérica."},
            {"nombre": "Navarra", "codigo": "NC", "imagen": "navarra.jpg", "descripcion": "Navarra es una comunidad foral española situada en el norte de la península ibérica."},
            {"nombre": "País Vasco", "codigo": "PV", "imagen": "paisvasco.jpg", "descripcion": "País Vasco es una comunidad autónoma española situada en el norte de la península ibérica."},
            {"nombre": "La Rioja", "codigo": "RI", "imagen": "larioja.jpg", "descripcion": "La Rioja es una comunidad autónoma española situada en el norte de la península ibérica."},
            {"nombre": "Valencia", "codigo": "VC", "imagen": "valencia.jpg", "descripcion": "Valencia es una comunidad autónoma española situada en el este de la península ibérica."},
            {"nombre": "Ceuta", "codigo": "CE", "imagen": "ceuta.jpg", "descripcion": "Ceuta es una ciudad autónoma española situada en el norte de África."},
            {"nombre": "Melilla", "codigo": "ML", "imagen": "melilla.jpg", "descripcion": "Melilla es una ciudad autónoma española situada en el norte de África."},
        ]
            # eliminar los modelos de comunidad
        ComunidadAutonoma.objects.all().delete()
        MediaFile.objects.all().delete()

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
                    "descripcion": comunidad["descripcion"],
                    "imagen": media_file,
                }
            )

            # Mostrar el estado en la consola
            if created:
                self.stdout.write(self.style.SUCCESS(f'Comunidad creada: {comunidad["nombre"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Comunidad actualizada: {comunidad["nombre"]}'))

        self.stdout.write(self.style.SUCCESS('¡Todas las comunidades han sido procesadas con imágenes!'))
