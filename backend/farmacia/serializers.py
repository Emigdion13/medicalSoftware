from rest_framework import serializers
from farmacia.models import (
    Medicamento, InventarioFarmacia, RegistroMedico,
    RecetaMedicamento, DispensacionMedicamentos
)


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = [
            'id', 'nombre_generico', 'nombre_comercial',
            'formula_quimica', 'laboratorio', 'descripcion'
        ]
        read_only_fields = ['id']


class InventarioFarmaciaSerializer(serializers.ModelSerializer):
    nombre_generico = serializers.CharField(
        source='medicamento.nombre_generico', read_only=True
    )

    class Meta:
        model = InventarioFarmacia
        fields = [
            'id', 'medicamento', 'nombre_generico', 'cantidad_stock',
            'nivel_minimo', 'precio_unitario', 'fecha_vencimiento',
            'proveedor', 'necesita_reponer'
        ]
        read_only_fields = ['id']


class RegistroMedicoSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.CharField(
        source='paciente.usuario.nombre_completo', read_only=True
    )
    doctor_nombre = serializers.CharField(
        source='doctor.nombre_completo', read_only=True
    )

    class Meta:
        model = RegistroMedico
        fields = [
            'id', 'paciente', 'paciente_nombre', 'fecha_registro',
            'diagnostico', 'tratamiento', 'doctor', 'doctor_nombre',
            'enfermera', 'datos_custom', 'seguimiento_requerido',
            'fecha_seguimiento', 'creado_el'
        ]
        read_only_fields = ['id', 'creado_el']


class RecetaMedicamentoSerializer(serializers.ModelSerializer):
    medicamento_nombre = serializers.CharField(
        source='medicamento.nombre_generico', read_only=True
    )

    class Meta:
        model = RecetaMedicamento
        fields = [
            'id', 'registro_medico', 'medicamento', 'medicamento_nombre',
            'dosis', 'frecuencia', 'duracion', 'notas'
        ]
        read_only_fields = ['id']


class DispensacionMedicamentosSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.CharField(
        source='paciente.usuario.nombre_completo', read_only=True
    )
    medicamento_nombre = serializers.CharField(
        source='medicamento.nombre_generico', read_only=True
    )

    class Meta:
        model = DispensacionMedicamentos
        fields = [
            'id', 'paciente', 'paciente_nombre', 'medicamento',
            'medicamento_nombre', 'cantidad', 'fecha_dispensa',
            'administrado_por', 'notas'
        ]
        read_only_fields = ['id']
