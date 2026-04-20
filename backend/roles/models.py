from django.db import models
from django.utils import timezone

class Role(models.Model):
    """ Tabla centralizada para gestionar los roles del sistema. """

    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre del rol")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción del rol")
    permisos = models.JSONField(default=list, verbose_name="Lista de permisos")
    creado_el = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
    actualizado_el = models.DateTimeField(default=timezone.now, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
