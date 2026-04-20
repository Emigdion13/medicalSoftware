"""
Admin configuration for personal.
"""

from django.contrib import admin
from pacientes.models import Personal


class PersonalAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'codigo_empleado', 'fecha_nacimiento', 'tipo_sangre')
    search_fields = ('usuario__nombre_completo', 'codigo_empleado')


admin.site.register(Personal, PersonalAdmin)
