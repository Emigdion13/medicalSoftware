"""
Modelos de la aplicación farmacia.
"""

from django.db import models
from pacientes.models import Paciente
from usuarios.models import Usuario


class InventarioFarmacia(models.Model):
    """ Modelo para el inventario de medicamentos. """
    
    nombre_medicamento = models.CharField(max_length=100, unique=True, 
                                          verbose_name='Nombre del Medicamento')
    nombre_generico = models.CharField(max_length=100, blank=True, 
                                       verbose_name='Nombre Genérico')
    cantidad_stock = models.IntegerField(default=0, verbose_name='Cantidad en Stock')
    nivel_minimo = models.IntegerField(default=5, verbose_name='Nivel Mínimo de Alerta')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, 
                                          verbose_name='Precio Unitario')
    fecha_vencimiento = models.DateField(blank=True, null=True, verbose_name='Fecha de Vencimiento')
    proveedor = models.CharField(max_length=100, blank=True, verbose_name='Proveedor')
    
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
    class Meta:
        verbose_name = 'Inventario Farmacia'
        verbose_name_plural = 'Inventarios Farmacia'
        ordering = ['nombre_medicamento']
    
    def __str__(self):
        return f'{self.nombre_medicamento} - Stock: {self.cantidad_stock}'
    
    @property
    def necesita_reponer(self):
        return self.cantidad_stock <= self.nivel_minimo


class DispensacionMedicamentos(models.Model):
    """ Modelo para el registro de entrega de medicamentos. """
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Paciente')
    inventario = models.ForeignKey(InventarioFarmacia, on_delete=models.CASCADE, 
                                   verbose_name='Medicamento')
    cantidad = models.IntegerField(verbose_name='Cantidad Entregada')
    fecha_dispensa = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Dispensa')
    administrado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True,
                                         related_name='dispensaciones', 
                                         verbose_name='Administrado por')
    notas = models.TextField(blank=True, verbose_name='Notas Adicionales')
    
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
    class Meta:
        verbose_name = 'Dispensación de Medicamentos'
        verbose_name_plural = 'Dispensaciones de Medicamentos'
        ordering = ['-fecha_dispensa']
    
    def __str__(self):
        return f'{self.cantidad}x {self.inventario.nombre_medicamento} para {self.paciente}'
