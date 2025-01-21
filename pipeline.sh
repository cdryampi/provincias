#!/bin/bash
echo "==== Iniciando pipeline ===="
echo "==== Instalando las variables de entorno ===="
python generate_env.py

echo "==== Ejecutando migraciones ===="
python manage.py migrate --noinput

echo "==== Ejecutando collectstatic ===="
python manage.py collectstatic --noinput

echo "==== Ajustando permisos para static y media ===="
chmod -R 755 static/
chmod -R 755 media/

echo "==== Ejecutando tareas de post-deploy ===="
python post_deploy.py

echo "==== Pipeline completada ===="
