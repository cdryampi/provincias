import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'provincias.settings')
django.setup()

from django.contrib.auth.models import User
from django.core.management import call_command

# Ejecutar el populate
print("Ejecutando el comando populate_comunidades...")
call_command('populate_comunidades')

# Crear un superusuario si no existe
SUPERUSER_NAME = os.getenv('DJANGO_SUPERUSER_NAME', 'admin')
SUPERUSER_EMAIL = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
SUPERUSER_PASSWORD = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin123')

if not User.objects.filter(username=SUPERUSER_NAME).exists():
    print(f"Creando superusuario: {SUPERUSER_NAME}")
    User.objects.create_superuser(
        username=SUPERUSER_NAME,
        email=SUPERUSER_EMAIL,
        password=SUPERUSER_PASSWORD,
    )
else:
    print(f"El superusuario {SUPERUSER_NAME} ya existe.")
