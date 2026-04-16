"""
Admin configuration for emergencias.
"""

from django.contrib import admin
from emergencias.models import Emergencia


class EmergenciaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tipo_alerta', 'estado', 'creado_el')
    list_filter = ('estado', 'tipo_alerta', 'creado_el')
    search_fields = ('paciente__usuario__nombre_completo', 'descripcion')


admin.site.register(Emergencia, EmergenciaAdmin)
