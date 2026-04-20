"""
Vistas de la aplicación citas.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cita
from .serializers import CitaSerializer


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


# ── JSON API Views (new) ────────────────────────────────────────

@api_view(['GET'])
def api_citas(request):
    """Obtener todas las citas."""
    citas = Cita.objects.select_related('paciente', 'doctor').all()
    serializer = CitaSerializer(citas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_cita_detalle(request, pk):
    """Obtener una cita por ID."""
    try:
        cita = Cita.objects.select_related('paciente', 'doctor').get(pk=pk)
    except Cita.DoesNotExist:
        return Response({'error': 'Cita no encontrada'}, status=404)
    serializer = CitaSerializer(cita)
    return Response(serializer.data)


@api_view(['POST'])
def api_citas_create(request):
    """Crear una nueva cita."""
    serializer = CitaSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    cita = serializer.save()
    return Response(CitaSerializer(cita).data, status=201)


@api_view(['PUT', 'PATCH'])
def api_cita_actualizar(request, pk):
    """Actualizar una cita."""
    try:
        cita = Cita.objects.get(pk=pk)
    except Cita.DoesNotExist:
        return Response({'error': 'Cita no encontrada'}, status=404)
    serializer = CitaSerializer(cita, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    cita = serializer.save()
    return Response(CitaSerializer(cita).data)


@api_view(['DELETE'])
def api_cita_eliminar(request, pk):
    """Eliminar una cita."""
    try:
        cita = Cita.objects.get(pk=pk)
        cita.delete()
        return Response({'message': 'Cita eliminada'}, status=204)
    except Cita.DoesNotExist:
        return Response({'error': 'Cita no encontrada'}, status=404)
