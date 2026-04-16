"""
Modelos de la aplicación citas.
"""

from django.db import models
from usuarios.models import Usuario
from pacientes.models import Paciente


class Cita(models.Model):
    """ Modelo para las citas médicas. """
    
    ESTADOS = [
        ('scheduled', 'Programada'),
        ('completed', 'Completada'),
        ('cancelled', 'Cancelada'),
    ]
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Paciente')
    doctor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, 
                               related_name='citas_atendidas', verbose_name='Doctor')
    fecha_cita = models.DateTimeField(verbose_name='Fecha y Hora de la Cita')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='scheduled', 
                              verbose_name='Estado')
    motivo = models.TextField(blank=True, verbose_name='Motivo de la Consulta')
    notas = models.TextField(blank=True, verbose_name='Notas Adicionales')
    
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['-fecha_cita']
    
    def __str__(self):
        return f'Cita de {self.paciente} con Dr. {self.doctor} - {self.fecha_cita}'
    
    @property
    def esta_vencida(self):
        from django.utils import timezone
        return self.fecha_cita < timezone.now() and self.estado == 'scheduled'
