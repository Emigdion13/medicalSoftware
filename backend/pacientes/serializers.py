from rest_framework import serializers
from pacientes.models import Personal


class PersonalSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.CharField(
        source='usuario.nombre_completo'
    )
    correo_electronico = serializers.EmailField(
        source='usuario.correo_electronico'
    )

    class Meta:
        model = Personal
        fields = [
            'id', 'usuario', 'nombre_completo', 'correo_electronico',
            'codigo_empleado', 'fecha_nacimiento', 'tipo_sangre',
            'nombre_contacto_emergencia', 'telefono_contacto_emergencia',
            'notas_medicas', 'creado_el'
        ]
        read_only_fields = ['id', 'creado_el']
