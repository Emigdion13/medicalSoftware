"""
Configuración de la aplicación farmacia.
"""

from django.apps import AppConfig


class FarmaciaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farmacia'
    verbose_name = 'Gestión de Farmacia'
