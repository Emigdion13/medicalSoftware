"""
Admin configuration for pacientes.
"""

from django.contrib import admin
from pacientes.models import Paciente


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'codigo_empleado', 'fecha_nacimiento', 'tipo_sangre')
    search_fields = ('usuario__nombre_completo', 'codigo_empleado')


admin.site.register(Paciente, PacienteAdmin)
