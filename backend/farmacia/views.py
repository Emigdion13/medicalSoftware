"""
Vistas de la aplicación farmacia.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Medicamento, InventarioFarmacia, RegistroMedico, RecetaMedicamento, DispensacionMedicamentos
from .serializers import (
    MedicamentoSerializer, InventarioFarmaciaSerializer,
    RegistroMedicoSerializer, RecetaMedicamentoSerializer, DispensacionMedicamentosSerializer
)


# ── HTML Template Views (existing) ───────────────────────────────

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


class DispensacionListView(ListView):
    model = DispensacionMedicamentos
    template_name = 'farmacia/dispensacion_list.html'
    context_object_name = 'dispensaciones'


class DispensacionCreateView(CreateView):
    model = DispensacionMedicamentos
    template_name = 'farmacia/dispensacion_form.html'
    fields = ['paciente', 'medicamento', 'cantidad', 'administrado_por', 'notas']
    success_url = reverse_lazy('farmacia:dispensacion_lista')


# ── JSON API Views (new) ───────────────────────────────────────

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_medicamentos(request):
    """Obtener todos los medicamentos."""
    medicamentos = Medicamento.objects.all()
    serializer = MedicamentoSerializer(medicamentos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_medicamento_detalle(request, pk):
    """Obtener un medicamento por ID."""
    try:
        medicamento = Medicamento.objects.get(pk=pk)
    except Medicamento.DoesNotExist:
        return Response({'error': 'Medicamento no encontrado'}, status=404)
    serializer = MedicamentoSerializer(medicamento)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_inventario(request):
    """Obtener todo el inventario."""
    inventarios = InventarioFarmacia.objects.select_related('medicamento').all()
    serializer = InventarioFarmaciaSerializer(inventarios, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_registros(request):
    """Obtener todos los registros médicos."""
    registros = RegistroMedico.objects.select_related('paciente', 'doctor').all()
    serializer = RegistroMedicoSerializer(registros, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_recetas(request):
    """Obtener todas las recetas."""
    recetas = RecetaMedicamento.objects.select_related('registro_medico', 'medicamento').all()
    serializer = RecetaMedicamentoSerializer(recetas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_dispensaciones(request):
    """Obtener todas las dispensaciones."""
    dispensaciones = DispensacionMedicamentos.objects.select_related('paciente', 'medicamento').all()
    serializer = DispensacionMedicamentosSerializer(dispensaciones, many=True)
    return Response(serializer.data)


# ── CRUD API Views (create/update/delete) ───────────────────────

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_medicamento_create(request):
    """Crear un nuevo medicamento."""
    serializer = MedicamentoSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    medicamento = serializer.save()
    return Response(MedicamentoSerializer(medicamento).data, status=201)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def api_medicamento_actualizar(request, pk):
    """Actualizar un medicamento."""
    try:
        medicamento = Medicamento.objects.get(pk=pk)
    except Medicamento.DoesNotExist:
        return Response({'error': 'Medicamento no encontrado'}, status=404)
    serializer = MedicamentoSerializer(medicamento, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    medicamento = serializer.save()
    return Response(MedicamentoSerializer(medicamento).data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_medicamento_eliminar(request, pk):
    """Eliminar un medicamento."""
    try:
        medicamento = Medicamento.objects.get(pk=pk)
        medicamento.delete()
        return Response({'message': 'Medicamento eliminado'}, status=204)
    except Medicamento.DoesNotExist:
        return Response({'error': 'Medicamento no encontrado'}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_inventario_create(request):
    """Crear un nuevo inventario."""
    serializer = InventarioFarmaciaSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    inventario = serializer.save()
    return Response(InventarioFarmaciaSerializer(inventario).data, status=201)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def api_inventario_actualizar(request, pk):
    """Actualizar un inventario."""
    try:
        inventario = InventarioFarmacia.objects.get(pk=pk)
    except InventarioFarmacia.DoesNotExist:
        return Response({'error': 'Inventario no encontrado'}, status=404)
    serializer = InventarioFarmaciaSerializer(inventario, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    inventario = serializer.save()
    return Response(InventarioFarmaciaSerializer(inventario).data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_inventario_eliminar(request, pk):
    """Eliminar un inventario."""
    try:
        inventario = InventarioFarmacia.objects.get(pk=pk)
        inventario.delete()
        return Response({'message': 'Inventario eliminado'}, status=204)
    except InventarioFarmacia.DoesNotExist:
        return Response({'error': 'Inventario no encontrado'}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_registro_create(request):
    """Crear un nuevo registro médico."""
    serializer = RegistroMedicoSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    registro = serializer.save()
    return Response(RegistroMedicoSerializer(registro).data, status=201)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_registro_detalle(request, pk):
    """Obtener un registro médico por ID."""
    try:
        registro = RegistroMedico.objects.select_related('paciente', 'doctor').get(pk=pk)
    except RegistroMedico.DoesNotExist:
        return Response({'error': 'Registro no encontrado'}, status=404)
    serializer = RegistroMedicoSerializer(registro)
    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def api_registro_actualizar(request, pk):
    """Actualizar un registro médico."""
    try:
        registro = RegistroMedico.objects.get(pk=pk)
    except RegistroMedico.DoesNotExist:
        return Response({'error': 'Registro no encontrado'}, status=404)
    serializer = RegistroMedicoSerializer(registro, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    registro = serializer.save()
    return Response(RegistroMedicoSerializer(registro).data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_registro_eliminar(request, pk):
    """Eliminar un registro médico."""
    try:
        registro = RegistroMedico.objects.get(pk=pk)
        registro.delete()
        return Response({'message': 'Registro eliminado'}, status=204)
    except RegistroMedico.DoesNotExist:
        return Response({'error': 'Registro no encontrado'}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_receta_create(request):
    """Crear una nueva receta."""
    serializer = RecetaMedicamentoSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    receta = serializer.save()
    return Response(RecetaMedicamentoSerializer(receta).data, status=201)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_receta_detalle(request, pk):
    """Obtener una receta por ID."""
    try:
        receta = RecetaMedicamento.objects.select_related('registro_medico', 'medicamento').get(pk=pk)
    except RecetaMedicamento.DoesNotExist:
        return Response({'error': 'Receta no encontrada'}, status=404)
    serializer = RecetaMedicamentoSerializer(receta)
    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def api_receta_actualizar(request, pk):
    """Actualizar una receta."""
    try:
        receta = RecetaMedicamento.objects.get(pk=pk)
    except RecetaMedicamento.DoesNotExist:
        return Response({'error': 'Receta no encontrada'}, status=404)
    serializer = RecetaMedicamentoSerializer(receta, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    receta = serializer.save()
    return Response(RecetaMedicamentoSerializer(receta).data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_receta_eliminar(request, pk):
    """Eliminar una receta."""
    try:
        receta = RecetaMedicamento.objects.get(pk=pk)
        receta.delete()
        return Response({'message': 'Receta eliminada'}, status=204)
    except RecetaMedicamento.DoesNotExist:
        return Response({'error': 'Receta no encontrada'}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_dispensacion_create(request):
    """Crear una nueva dispensación."""
    serializer = DispensacionMedicamentosSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    dispensacion = serializer.save()
    return Response(DispensacionMedicamentosSerializer(dispensacion).data, status=201)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_dispensacion_detalle(request, pk):
    """Obtener una dispensación por ID."""
    try:
        dispensacion = DispensacionMedicamentos.objects.select_related('paciente', 'medicamento').get(pk=pk)
    except DispensacionMedicamentos.DoesNotExist:
        return Response({'error': 'Dispensación no encontrada'}, status=404)
    serializer = DispensacionMedicamentosSerializer(dispensacion)
    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def api_dispensacion_actualizar(request, pk):
    """Actualizar una dispensación."""
    try:
        dispensacion = DispensacionMedicamentos.objects.get(pk=pk)
    except DispensacionMedicamentos.DoesNotExist:
        return Response({'error': 'Dispensación no encontrada'}, status=404)
    serializer = DispensacionMedicamentosSerializer(dispensacion, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    dispensacion = serializer.save()
    return Response(DispensacionMedicamentosSerializer(dispensacion).data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_dispensacion_eliminar(request, pk):
    """Eliminar una dispensación."""
    try:
        dispensacion = DispensacionMedicamentos.objects.get(pk=pk)
        dispensacion.delete()
        return Response({'message': 'Dispensación eliminada'}, status=204)
    except DispensacionMedicamentos.DoesNotExist:
        return Response({'error': 'Dispensación no encontrada'}, status=404)
