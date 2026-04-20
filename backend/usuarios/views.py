"""
Vistas de la aplicación usuarios.
"""

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario


class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'


class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/usuario_detail.html'
    context_object_name = 'usuario'


class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuarios/usuario_form.html'
    fields = ['usuario', 'correo_electronico', 'nombre_completo', 'numero_telefono', 'rol', 'esta_activo']
    success_url = reverse_lazy('usuarios:lista')


class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuarios/usuario_form.html'
    fields = ['usuario', 'correo_electronico', 'nombre_completo', 'numero_telefono', 'rol', 'esta_activo']
    success_url = reverse_lazy('usuarios:lista')


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuarios:lista')
