"""
Admin configuration for emergencias.
"""

from django.contrib import admin
from emergencias.models import Emergencia


class EmergenciaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tipo_alerta', 'estado')
    search_fields = ('paciente__codigo_empleado', 'descripcion')


admin.site.register(Emergencia, EmergenciaAdmin)
