"""
Vistas de la aplicación emergencias.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Emergencia
from .serializers import EmergenciaSerializer


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


# ── API Views (new) ───────────────────────────────────────────────

@api_view(['GET'])
def api_emergencias(request):
    """Obtener todas las emergencias."""
    emergencias = Emergencia.objects.select_related('paciente').all()
    serializer = EmergenciaSerializer(emergencias, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_emergencia_detalle(request, pk):
    """Obtener una emergencia por ID."""
    try:
        emergencia = Emergencia.objects.select_related('paciente').get(pk=pk)
    except Emergencia.DoesNotExist:
        return Response({'error': 'Emergencia no encontrada'}, status=404)
    serializer = EmergenciaSerializer(emergencia)
    return Response(serializer.data)


@api_view(['POST'])
def api_emergencia_create(request):
    """Crear una nueva emergencia."""
    serializer = EmergenciaSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    emergencia = serializer.save()
    return Response(EmergenciaSerializer(emergencia).data, status=201)


@api_view(['PUT', 'PATCH'])
def api_emergencia_actualizar(request, pk):
    """Actualizar una emergencia."""
    try:
        emergencia = Emergencia.objects.get(pk=pk)
    except Emergencia.DoesNotExist:
        return Response({'error': 'Emergencia no encontrada'}, status=404)
    serializer = EmergenciaSerializer(emergencia, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    emergencia = serializer.save()
    return Response(EmergenciaSerializer(emergencia).data)


@api_view(['DELETE'])
def api_emergencia_eliminar(request, pk):
    """Eliminar una emergencia."""
    try:
        emergencia = Emergencia.objects.get(pk=pk)
        emergencia.delete()
        return Response({'message': 'Emergencia eliminada'}, status=204)
    except Emergencia.DoesNotExist:
        return Response({'error': 'Emergencia no encontrada'}, status=404)
