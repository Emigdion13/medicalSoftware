# README del Sistema Médico Interno

## Instalación

1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar: `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Linux/Mac)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Configurar PostgreSQL
6. Aplicar migraciones: `python manage.py migrate`
7. Crear superusuario: `python manage.py createsuperuser`
8. Ejecutar servidor: `python manage.py runserver`

## Estructura

- **backend**: Django API
- **frontend**: React.js (pendiente)

## Endpoints disponibles

- `/admin/` - Panel de administración
- `/api/usuarios/` - Gestión de usuarios
- `/api/pacientes/` - Gestión de pacientes
- `/api/citas/` - Gestión de citas
- `/api/emergencias/` - Alertas y emergencias
- `/api/farmacia/` - Farmacia e inventario

## Tecnologías

- Python 3.10+
- Django 4.2+
- PostgreSQL
