"""
Vistas de la aplicación emergencias.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Emergencia


class EmergenciaListView(ListView):
    model = Emergencia
    template_name = 'emergencias/emergencia_list.html'
    context_object_name = 'emergencias'
    
    def get_queryset(self):
        return Emergencia.objects.select_related('paciente')


class EmergenciaDetailView(DetailView):
    model = Emergencia
    template_name = 'emergencias/emergencia_detail.html'
    context_object_name = 'emergencia'


class EmergenciaCreateView(CreateView):
    model = Emergencia
    template_name = 'emergencias/emergencia_form.html'
    fields = ['paciente', 'tipo_alerta', 'descripcion', 'estado', 'equipo_responsable']
    success_url = reverse_lazy('emergencias:lista')


class EmergenciaUpdateView(UpdateView):
    model = Emergencia
    template_name = 'emergencias/emergencia_form.html'
    fields = ['paciente', 'tipo_alerta', 'descripcion', 'estado', 'equipo_responsable']
    success_url = reverse_lazy('emergencias:lista')


class EmergenciaDeleteView(DeleteView):
    model = Emergencia
    template_name = 'emergencias/emergencia_confirm_delete.html'
    success_url = reverse_lazy('emergencias:lista')
