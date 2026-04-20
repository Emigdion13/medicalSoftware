"""
Admin configuration for citas.
"""

from django.contrib import admin
from citas.models import Cita


class CitaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'fecha_cita', 'estado')
    list_filter = ('estado',)
    search_fields = ('paciente__codigo_empleado', 'motivo')


admin.site.register(Cita, CitaAdmin)
