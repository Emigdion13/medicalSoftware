from django.db import models
from django.utils import timezone


class Emergencia(models.Model):
    """ Modelo para las alertas y manejo de emergencias médicas. """

    TIPO_ALERTA_CHOICES = [
        ("heart_attack", "Infarto"),
        ("accident", "Accidente"),
        ("stroke", "Accidente Cerebrovascular"),
        ("allergic_reaction", "Reacción Alérgica"),
        ("respiratory", "Problema Respiratorio"),
        ("other", "Otro"),
    ]

    ESTADOS = [
        ("active", "Activo"),
        ("resolved", "Resuelto"),
        ("ignored", "Ignorado"),
    ]

    paciente = models.ForeignKey("pacientes.Personal", on_delete=models.CASCADE, verbose_name="Paciente")
    tipo_alerta = models.CharField(max_length=50, choices=TIPO_ALERTA_CHOICES,
                                   verbose_name="Tipo de Alerta")
    descripcion = models.TextField(verbose_name="Descripción del Evento")
    estado = models.CharField(max_length=20, choices=ESTADOS, default="active",
                              verbose_name="Estado")
    equipo_responsable = models.JSONField(blank=True, null=True,
                                          verbose_name="Equipo Responsable")
    hora_respuesta = models.DateTimeField(blank=True, null=True, verbose_name="Hora de Respuesta")
    resuelto_el = models.DateTimeField(blank=True, null=True, verbose_name="Resuelto el")

    creado_el = models.DateTimeField(default=timezone.now, verbose_name="Creado el")
    actualizado_el = models.DateTimeField(default=timezone.now, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Emergencia"
        verbose_name_plural = "Emergencias"
        ordering = ["-creado_el"]

    def __str__(self):
        return f"Emergencia de {self.paciente} - {self.tipo_alerta}"

    @property
    def tiempo_respuesta(self):
        if self.hora_respuesta and self.creado_el:
            delta = self.hora_respuesta - self.creado_el
            return delta.total_seconds() / 60
        return None
