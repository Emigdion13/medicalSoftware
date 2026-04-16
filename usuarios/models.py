"""
Modelos de la aplicación usuarios.
"""

from django.db import models


class Usuario(models.Model):
    """ Modelo para los usuarios del sistema médico. """
    
    ROLES = [
        ('staff', 'Personal'),
        ('doctor', 'Médico'),
        ('admin', 'Administrador'),
    ]
    
    usuario = models.CharField(max_length=50, unique=True, verbose_name='Usuario')
    correo_electronico = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    nombre_completo = models.CharField(max_length=100, verbose_name='Nombre Completo')
    numero_telefono = models.CharField(max_length=20, blank=True, verbose_name='Número de Teléfono')
    rol = models.CharField(max_length=20, choices=ROLES, default='staff', verbose_name='Rol')
    esta_activo = models.BooleanField(default=True, verbose_name='¿Está Activo?')
    
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre_completo']
    
    def __str__(self):
        return f'{self.nombre_completo} ({self.usuario})'

    def get_short_name(self):
        return self.usuario
