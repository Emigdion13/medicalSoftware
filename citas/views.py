"""
Vistas de la aplicación citas.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cita


class CitaListView(ListView):
    model = Cita
    template_name = 'citas/cita_list.html'
    context_object_name = 'citas'
    
    def get_queryset(self):
        return Cita.objects.select_related('paciente', 'doctor')


class CitaDetailView(DetailView):
    model = Cita
    template_name = 'citas/cita_detail.html'
    context_object_name = 'cita'


class CitaCreateView(CreateView):
    model = Cita
    template_name = 'citas/cita_form.html'
    fields = ['paciente', 'doctor', 'fecha_cita', 'estado', 'motivo', 'notas']
    success_url = reverse_lazy('citas:lista')


class CitaUpdateView(UpdateView):
    model = Cita
    template_name = 'citas/cita_form.html'
    fields = ['paciente', 'doctor', 'fecha_cita', 'estado', 'motivo', 'notas']
    success_url = reverse_lazy('citas:lista')


class CitaDeleteView(DeleteView):
    model = Cita
    template_name = 'citas/cita_confirm_delete.html'
    success_url = reverse_lazy('citas:lista')
