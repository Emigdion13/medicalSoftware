"""
Vistas de la aplicación farmacia.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Medicamento, InventarioFarmacia, RegistroMedico, RecetaMedicamento, DispensacionMedicamentos


# Vistas para Medicamentos (Catálogo)
class MedicamentoListView(ListView):
    model = Medicamento
    template_name = 'farmacia/medicamento_list.html'
    context_object_name = 'medicamentos'


class MedicamentoDetailView(DetailView):
    model = Medicamento
    template_name = 'farmacia/medicamento_detail.html'
    context_object_name = 'medicamento'


class MedicamentoCreateView(CreateView):
    model = Medicamento
    template_name = 'farmacia/medicamento_form.html'
    fields = ['nombre_generico', 'nombre_comercial', 'formula_quimica', 'laboratorio', 'descripcion']
    success_url = reverse_lazy('farmacia:medicamento_lista')


class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    template_name = 'farmacia/medicamento_form.html'
    fields = ['nombre_generico', 'nombre_comercial', 'formula_quimica', 'laboratorio', 'descripcion']
    success_url = reverse_lazy('farmacia:medicamento_lista')


class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    template_name = 'farmacia/medicamento_confirm_delete.html'
    success_url = reverse_lazy('farmacia:medicamento_lista')


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
    fields = ['medicamento', 'cantidad_stock', 'nivel_minimo', 
              'precio_unitario', 'fecha_vencimiento', 'proveedor']
    success_url = reverse_lazy('farmacia:inventario_lista')


class InventarioUpdateView(UpdateView):
    model = InventarioFarmacia
    template_name = 'farmacia/inventario_form.html'
    fields = ['medicamento', 'cantidad_stock', 'nivel_minimo',
              'precio_unitario', 'fecha_vencimiento', 'proveedor']
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
    fields = ['paciente', 'medicamento', 'cantidad', 'administrado_por', 'notas']
    success_url = reverse_lazy('farmacia:dispensacion_lista')
