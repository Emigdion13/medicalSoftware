"""
Vistas de la aplicación farmacia.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import InventarioFarmacia, DispensacionMedicamentos


# Vistas para Inventario Farmacia
class InventarioListView(ListView):
    model = InventarioFarmacia
    template_name = 'farmacia/inventario_list.html'
    context_object_name = 'inventarios'


class InventarioDetailView(DetailView):
    model = InventarioFarmacia
    template_name = 'farmacia/inventario_detail.html'
    context_object_name = 'inventario'


class InventarioCreateView(CreateView):
    model = InventarioFarmacia
    template_name = 'farmacia/inventario_form.html'
    fields = ['nombre_medicamento', 'nombre_generico', 'cantidad_stock', 
              'nivel_minimo', 'precio_unitario', 'fecha_vencimiento', 'proveedor']
    success_url = reverse_lazy('farmacia:inventario_lista')


class InventarioUpdateView(UpdateView):
    model = InventarioFarmacia
    template_name = 'farmacia/inventario_form.html'
    fields = ['nombre_medicamento', 'nombre_generico', 'cantidad_stock',
              'nivel_minimo', 'precio_unitario', 'fecha_vencimiento', 'proveedor']
    success_url = reverse_lazy('farmacia:inventario_lista')


class InventarioDeleteView(DeleteView):
    model = InventarioFarmacia
    template_name = 'farmacia/inventario_confirm_delete.html'
    success_url = reverse_lazy('farmacia:inventario_lista')


# Vistas para Dispensación de Medicamentos
class DispensacionListView(ListView):
    model = DispensacionMedicamentos
    template_name = 'farmacia/dispensacion_list.html'
    context_object_name = 'dispensaciones'


class DispensacionCreateView(CreateView):
    model = DispensacionMedicamentos
    template_name = 'farmacia/dispensacion_form.html'
    fields = ['paciente', 'inventario', 'cantidad', 'administrado_por', 'notas']
    success_url = reverse_lazy('farmacia:dispensacion_lista')
