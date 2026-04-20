from rest_framework import serializers
from usuarios.models import Usuario
from roles.models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'nombre', 'descripcion']


class UsuarioSerializer(serializers.ModelSerializer):
    rol = RoleSerializer(read_only=True)
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source='rol', write_only=True, required=False
    )

    class Meta:
        model = Usuario
        fields = [
            'id', 'usuario', 'correo_electronico', 'nombre_completo',
            'numero_telefono', 'rol', 'rol_id', 'esta_activo', 'creado_el'
        ]
        read_only_fields = ['id', 'creado_el']


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField()
    nombre_completo = serializers.CharField(max_length=100)
    correo_electronico = serializers.EmailField()
    numero_telefono = serializers.CharField(max_length=20, required=False)
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), required=False
    )
