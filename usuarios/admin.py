"""
Admin configuration for medic_system.
"""

from django.contrib import admin
from usuarios.models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'usuario', 'correo_electronico', 'rol', 'esta_activo')
    list_filter = ('rol', 'esta_activo')
    search_fields = ('nombre_completo', 'usuario', 'correo_electronico')


admin.site.register(Usuario, UsuarioAdmin)
