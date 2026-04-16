"""
Vistas de la aplicación pacientes.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente


class PacienteListView(ListView):
    model = Paciente
    template_name = 'pacientes/paciente_list.html'
    context_object_name = 'pacientes'


class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'pacientes/paciente_detail.html'
    context_object_name = 'paciente'


class PacienteCreateView(CreateView):
    model = Paciente
    template_name = 'pacientes/paciente_form.html'
    fields = ['usuario', 'codigo_empleado', 'fecha_nacimiento', 'tipo_sangre', 
              'nombre_contacto_emergencia', 'telefono_contacto_emergencia', 'notas_medicas']
    success_url = reverse_lazy('pacientes:lista')


class PacienteUpdateView(UpdateView):
    model = Paciente
    template_name = 'pacientes/paciente_form.html'
    fields = ['usuario', 'codigo_empleado', 'fecha_nacimiento', 'tipo_sangre',
              'nombre_contacto_emergencia', 'telefono_contacto_emergencia', 'notas_medicas']
    success_url = reverse_lazy('pacientes:lista')


class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'pacientes/paciente_confirm_delete.html'
    success_url = reverse_lazy('pacientes:lista')
