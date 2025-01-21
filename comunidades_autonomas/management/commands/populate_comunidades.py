from django.core.management.base import BaseCommand
from comunidades_autonomas.models import ComunidadAutonoma

class Command(BaseCommand):
    help = "Populate Comunidades Autónomas"

    def handle(self, *args, **options):
        comunidades = [
            {"nombre": "Andalucía", "codigo": "AN"},
            {"nombre": "Aragón", "codigo": "AR"},
            {"nombre": "Asturias", "codigo": "AS"},
            {"nombre": "Cantabria", "codigo": "CB"},
            {"nombre": "Castilla-La Mancha", "codigo": "CM"},
            {"nombre": "Castilla y León", "codigo": "CL"},
            {"nombre": "Cataluña", "codigo": "CT"},
            {"nombre": "Extremadura", "codigo": "EX"},
            {"nombre": "Galicia", "codigo": "GA"},
            {"nombre": "La Rioja", "codigo": "RI"},
            {"nombre": "Madrid", "codigo": "MD"},
            {"nombre": "Murcia", "codigo": "MU"},
            {"nombre": "Navarra", "codigo": "NC"},
            {"nombre": "País Vasco", "codigo": "PV"},
            {"nombre": "Valencia", "codigo": "VC"},
            {"nombre": "Ceuta", "codigo": "CE"},
            {"nombre": "Melilla", "codigo": "ML"},
        ]
        for comunidad in comunidades:
            obj, created = ComunidadAutonoma.objects.get_or_create(
                nombre=comunidad["nombre"],
                codigo=comunidad["codigo"]
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Comunidad Autónoma '{obj.nombre}' creada correctamente"))
            else:
                self.stdout.write(self.style.WARNING(f"Comunidad Autónoma '{obj.nombre}' ya existe"))

        self.stdout.write(self.style.SUCCESS("Comunidades Autónomas creadas correctamente"))
