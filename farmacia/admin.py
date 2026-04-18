"""
Admin configuration for farmacia.
"""

from django.contrib import admin
from farmacia.models import InventarioFarmacia, DispensacionMedicamentos


class InventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_medicamento', 'cantidad_stock', 'nivel_minimo', 'precio_unitario', 
                    'necesita_reponer')
    search_fields = ('nombre_medicamento', 'nombre_generico')



class DispensacionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'fecha_dispensa', 'cantidad')
    list_filter = ('fecha_dispensa',)
    search_fields = ('paciente__usuario__nombre_completo', 'inventario__nombre_medicamento')


admin.site.register(InventarioFarmacia, InventarioAdmin)
admin.site.register(DispensacionMedicamentos, DispensacionAdmin)
