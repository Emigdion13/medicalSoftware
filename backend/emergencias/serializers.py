from rest_framework import serializers
from emergencias.models import Emergencia


class EmergenciaSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.CharField(
        source='paciente.usuario.nombre_completo', read_only=True
    )

    class Meta:
        model = Emergencia
        fields = [
            'id', 'paciente', 'paciente_nombre', 'tipo_alerta',
            'descripcion', 'estado', 'equipo_responsable',
            'hora_respuesta', 'resuelto_el', 'tiempo_respuesta',
            'creado_el'
        ]
        read_only_fields = ['id', 'creado_el']
