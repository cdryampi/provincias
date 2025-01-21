import os

# Especificar las variables de entorno que necesitas
variables = [
    "DJANGO_SECRET_KEY",
    "DJANGO_SUPERUSER_EMAIL",
    "DJANGO_SUPERUSER_NAME",
    "DJANGO_SUPERUSER_PASSWORD",
    "DEBUG",
]

# Generar contenido del archivo .env
env_content = []
for var in variables:
    value = os.getenv(var, None)
    if value:
        env_content.append(f"{var}={value}")
    else:
        print(f"Advertencia: La variable {var} no está configurada en el entorno.")

# Escribir el archivo .env
if env_content:
    with open(".env", "w") as env_file:
        env_file.write("\n".join(env_content))
    print(".env generado correctamente.")
else:
    print("No se generó el archivo .env porque no se encontraron variables.")
