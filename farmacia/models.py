from django.db import models
from pacientes.models import Personal
from usuarios.models import Usuario


class Medicamento(models.Model):
    ''' Catálogo estandarizado de medicamentos. '''

    nombre_generico = models.CharField(max_length=100, unique=True, verbose_name='Nombre Genérico')
    nombre_comercial = models.CharField(max_length=100, blank=True, verbose_name='Nombre Comercial')
    formula_quimica = models.TextField(blank=True, verbose_name='Fórmula Química')
    laboratorio = models.CharField(max_length=100, blank=True, verbose_name='Laboratorio')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')

    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering = ['nombre_generico']

    def __str__(self):
        return self.nombre_generico


class InventarioFarmacia(models.Model):
    ''' Inventario de medicamentos disponibles (stock, precio, proveedor). '''

    medicamento = models.OneToOneField(Medicamento, on_delete=models.CASCADE, 
                                       related_name='inventario', verbose_name='Medicamento')
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
        ordering = ['medicamento__nombre_generico']

    def __str__(self):
        return f'{self.medicamento.nombre_generico} - Stock: {self.cantidad_stock}'

    @property
    def necesita_reponer(self):
        return self.cantidad_stock <= self.nivel_minimo


class RegistroMedico(models.Model):
    ''' Historial clínico completo del paciente. '''

    paciente = models.ForeignKey(Personal, on_delete=models.CASCADE, verbose_name='Paciente')
    fecha_registro = models.DateField(verbose_name='Fecha del Registro')
    diagnostico = models.TextField(verbose_name='Diagnóstico')
    tratamiento = models.TextField(blank=True, verbose_name='Tratamiento Prescrito')
    doctor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True,
                               related_name='registros_medicos', verbose_name='Médico')
    enfermera = models.CharField(max_length=100, blank=True, verbose_name='Enfermera Atendiente')
    datos_custom = models.JSONField(default=dict, verbose_name='Datos Personalizados')
    seguimiento_requerido = models.BooleanField(default=False, verbose_name='¿Requiere Seguimiento?')
    fecha_seguimiento = models.DateField(blank=True, null=True, verbose_name='Fecha de Seguimiento')

    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Registro Médico'
        verbose_name_plural = 'Registros Médicos'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f'Registro de {self.paciente} - {self.fecha_registro}'


class RecetaMedicamento(models.Model):
    ''' Relación muchos a muchos entre registros médicos y medicamentos. '''

    registro_medico = models.ForeignKey(RegistroMedico, on_delete=models.CASCADE, 
                                        related_name='recetas', verbose_name='Registro Médico')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT, 
                                    verbose_name='Medicamento')
    dosis = models.CharField(max_length=50, verbose_name='Dosis Indicada')
    frecuencia = models.CharField(max_length=50, verbose_name='Frecuencia de Toma')
    duracion = models.CharField(max_length=50, verbose_name='Duración del Tratamiento')
    notas = models.TextField(blank=True, verbose_name='Notas Adicionales')

    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Receta de Medicamento'
        verbose_name_plural = 'Recetas de Medicamentos'

    def __str__(self):
        return f'{self.medicamento.nombre_generico} para {self.registro_medico.paciente}'


class DispensacionMedicamentos(models.Model):
    ''' Registro de entrega de medicamentos a pacientes. '''

    paciente = models.ForeignKey(Personal, on_delete=models.CASCADE, verbose_name='Paciente')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT, 
                                    verbose_name='Medicamento')
    cantidad = models.IntegerField(verbose_name='Cantidad Entregada')
    fecha_dispensa = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Dispensa')
    administrado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True,
                                         related_name='dispensaciones', 
                                         verbose_name='Administrado por')
    notas = models.TextField(blank=True, verbose_name='Notas Adicionales')

    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Dispensación de Medicamentos'
        verbose_name_plural = 'Dispensaciones de Medicamentos'
        ordering = ['-fecha_dispensa']

    def __str__(self):
        return f'{self.cantidad}x {self.medicamento.nombre_generico} para {self.paciente}'
