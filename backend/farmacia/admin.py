"""
Admin configuration for farmacia.
"""

from django.contrib import admin
from farmacia.models import Medicamento, InventarioFarmacia, RegistroMedico, RecetaMedicamento, DispensacionMedicamentos


class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_generico', 'nombre_comercial', 'laboratorio')
    search_fields = ('nombre_generico', 'nombre_comercial')


class InventarioAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'cantidad_stock', 'nivel_minimo', 'precio_unitario', 
                    'necesita_reponer', 'fecha_vencimiento')
    search_fields = ('medicamento__nombre_generico',)


class RegistroMedicoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_registro', 'doctor', 'seguimiento_requerido')
    list_filter = ('fecha_registro', 'seguimiento_requerido')
    search_fields = ('paciente__codigo_empleado', 'diagnostico')


class RecetaMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'registro_medico', 'dosis', 'frecuencia', 'duracion')
    search_fields = ('medicamento__nombre_generico', 'registro_medico__paciente__codigo_empleado')


class DispensacionAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medicamento', 'cantidad', 'fecha_dispensa', 'administrado_por')
    list_filter = ('fecha_dispensa',)
    search_fields = ('paciente__codigo_empleado', 'medicamento__nombre_generico')


admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(InventarioFarmacia, InventarioAdmin)
admin.site.register(RegistroMedico, RegistroMedicoAdmin)
admin.site.register(RecetaMedicamento, RecetaMedicamentoAdmin)
admin.site.register(DispensacionMedicamentos, DispensacionAdmin)
