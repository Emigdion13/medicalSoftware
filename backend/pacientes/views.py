"""
Vistas de la aplicación personal.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Personal


class PersonalListView(ListView):
    model = Personal
    template_name = 'pacientes/personal_list.html'
    context_object_name = 'personales'


class PersonalDetailView(DetailView):
    model = Personal
    template_name = 'pacientes/personal_detail.html'
    context_object_name = 'personal'


class PersonalCreateView(CreateView):
    model = Personal
    template_name = 'pacientes/personal_form.html'
    fields = ['usuario', 'codigo_empleado', 'fecha_nacimiento', 'tipo_sangre',
              'nombre_contacto_emergencia', 'telefono_contacto_emergencia', 'notas_medicas']
    success_url = reverse_lazy('pacientes:lista')


class PersonalUpdateView(UpdateView):
    model = Personal
    template_name = 'pacientes/personal_form.html'
    fields = ['usuario', 'codigo_empleado', 'fecha_nacimiento', 'tipo_sangre',
              'nombre_contacto_emergencia', 'telefono_contacto_emergencia', 'notas_medicas']
    success_url = reverse_lazy('pacientes:lista')


class PersonalDeleteView(DeleteView):
    model = Personal
    template_name = 'pacientes/personal_confirm_delete.html'
    success_url = reverse_lazy('pacientes:lista')
