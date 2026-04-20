#!/bin/sh
set -e

echo "Waiting for database..."
until psql -h "$DATABASE_HOST" -U "$DATABASE_USER" -d "$DATABASE_NAME" -c '\q' 2>/dev/null; do
  sleep 1
done

echo "Database is up, running migrations..."
python manage.py migrate --noinput

echo "Creating superuser if needed..."
python -c "
from django.conf import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medic_system.settings')
import django
django.setup()
from usuarios.models import Usuario
if not Usuario.objects.filter(usuario='admin').exists():
    admin = Usuario(
        usuario='admin',
        correo_electronico='admin@centromedico.com',
        nombre_completo='Administrador del Sistema',
        esta_activo=True
    )
    admin.set_password('admin1234')
    admin.save()
    print('Admin user created: admin@centromedico.com / admin1234')
else:
    print('Admin user already exists')
"

echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000
