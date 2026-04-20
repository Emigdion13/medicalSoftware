"""
Vistas de la aplicación personal.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Personal
from .serializers import PersonalSerializer


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


# ── JSON API Views (new) ────────────────────────────────────────

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_personal(request):
    """Obtener todos los pacientes (personal)."""
    personales = Personal.objects.select_related('usuario').all()
    serializer = PersonalSerializer(personales, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_personal_detalle(request, pk):
    """Obtener un paciente por ID."""
    try:
        personal = Personal.objects.select_related('usuario').get(pk=pk)
    except Personal.DoesNotExist:
        return Response({'error': 'Paciente no encontrado'}, status=404)
    serializer = PersonalSerializer(personal)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_personal_create(request):
    """Crear un nuevo paciente."""
    serializer = PersonalSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    personal = serializer.save()
    return Response(PersonalSerializer(personal).data, status=201)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def api_personal_actualizar(request, pk):
    """Actualizar un paciente."""
    try:
        personal = Personal.objects.get(pk=pk)
    except Personal.DoesNotExist:
        return Response({'error': 'Paciente no encontrado'}, status=404)
    serializer = PersonalSerializer(personal, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    personal = serializer.save()
    return Response(PersonalSerializer(personal).data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_personal_eliminar(request, pk):
    """Eliminar un paciente."""
    try:
        personal = Personal.objects.get(pk=pk)
        personal.delete()
        return Response({'message': 'Paciente eliminado'}, status=204)
    except Personal.DoesNotExist:
        return Response({'error': 'Paciente no encontrado'}, status=404)
