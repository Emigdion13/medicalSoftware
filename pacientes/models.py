"""
Modelos de la aplicación pacientes.
"""

from django.db import models
from usuarios.models import Usuario


class Paciente(models.Model):
    """ Modelo para los pacientes (personal registrado). """
    
    usuario = models.OneToOneField(
        Usuario, 
        on_delete=models.CASCADE, 
        unique=True,
        verbose_name='Usuario'
    )
    codigo_empleado = models.CharField(max_length=20, unique=True, verbose_name='Código de Empleado')
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')
    tipo_sangre = models.CharField(max_length=3, blank=True, verbose_name='Tipo de Sangre')
    nombre_contacto_emergencia = models.CharField(max_length=100, blank=True, verbose_name='Contacto de Emergencia')
    telefono_contacto_emergencia = models.CharField(max_length=20, blank=True, verbose_name='Teléfono Contacto')
    notas_medicas = models.TextField(blank=True, verbose_name='Notas Médicas')
    
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['usuario__nombre_completo']
    
    def __str__(self):
        return f'{self.usuario.nombre_completo} ({self.codigo_empleado})'
