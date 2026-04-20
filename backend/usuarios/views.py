"""
Vistas de la aplicación usuarios.
"""

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.utils import timezone
import jwt

from .models import Usuario
from .serializers import (
    UsuarioSerializer, LoginRequestSerializer, RegisterRequestSerializer
)


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


# ── JSON API Views (new) ────────────────────────────────────────

@api_view(['GET'])
def api_usuarios(request):
    """Obtener todos los usuarios."""
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_usuario_detalle(request, pk):
    """Obtener un usuario por ID."""
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=404)
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    """Autenticar usuario y retornar token JWT."""
    serializer = LoginRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = authenticate(username=username, password=password)
    if user is None:
        # Intentar buscar por correo electrónico
        try:
            user = Usuario.objects.get(correo_electronico=username)
        except Usuario.DoesNotExist:
            return Response({'error': 'Credenciales inválidas'}, status=401)

    if not user.is_active:
        return Response({'error': 'Usuario desactivado'}, status=403)

    # Generar token JWT
    SECRET_KEY = 'medico-secret-key-2024'  # En producción, usar settings.SECRET_KEY
    payload = {
        'user_id': user.id,
        'username': user.usuario,
        'nombre': user.nombre_completo,
        'exp': timezone.now().timestamp() + 86400,  # 24 horas
        'iat': timezone.now().timestamp()
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return Response({
        'token': token,
        'user': {
            'id': user.id,
            'username': user.usuario,
            'nombre_completo': user.nombre_completo,
            'correo_electronico': user.correo_electronico,
            'esta_activo': user.esta_activo,
        }
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def api_register(request):
    """Registrar un nuevo usuario."""
    serializer = RegisterRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    # Verificar que el username no exista
    if Usuario.objects.filter(usuario=serializer.validated_data['username']).exists():
        return Response({'error': 'El nombre de usuario ya existe'}, status=409)

    if Usuario.objects.filter(correo_electronico=serializer.validated_data['correo_electronico']).exists():
        return Response({'error': 'El correo electrónico ya existe'}, status=409)

    # Crear usuario con contraseña segura
    from django.contrib.auth.hashers import make_password
    validated = serializer.validated_data.copy()
    password = validated.pop('password')

    rol = validated.get('rol_id')  # Puede ser None
    usuario = Usuario(
        **validated,
        esta_activo=True
    )
    usuario.set_password(password)  # Hash de contraseña
    if rol:
        usuario.rol = rol
    usuario.save()

    return Response(UsuarioSerializer(usuario).data, status=201)
