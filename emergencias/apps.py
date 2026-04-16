"""
Configuración de la aplicación emergencias.
"""

from django.apps import AppConfig


class EmergenciasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emergencias'
    verbose_name = 'Gestión de Emergencias'
