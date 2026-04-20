"""
Configuración de la aplicación citas.
"""

from django.apps import AppConfig


class CitasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'citas'
    verbose_name = 'Gestión de Citas'
