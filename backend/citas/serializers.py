from rest_framework import serializers
from citas.models import Cita


class CitaSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.CharField(
        source='paciente.usuario.nombre_completo', read_only=True
    )
    doctor_nombre = serializers.CharField(
        source='doctor.nombre_completo', read_only=True
    )

    class Meta:
        model = Cita
        fields = [
            'id', 'paciente', 'paciente_nombre', 'doctor', 'doctor_nombre',
            'fecha_cita', 'estado', 'motivo', 'notas', 'creado_el',
            'actualizado_el', 'esta_vencida'
        ]
        read_only_fields = ['id', 'creado_el', 'actualizado_el']
