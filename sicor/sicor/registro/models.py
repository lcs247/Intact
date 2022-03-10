import code
from pyexpat.errors import codes
from tabnanny import verbose
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.utils.html import format_html
# Create your models here.
#OPCIONES

ESTADO = [
    ('O','Operativo'),
    ('F','Fuera de Servicio'),
]


# PLANTAS
class Planta(models.Model):
    nombre = models.CharField('Planta', max_length=70, blank=False)
    codigo = models.CharField('Código', max_length=10, blank=False)
    descripcion = models.CharField('Descripción', max_length=70, blank=True)
    capacidad = models.CharField('Capacidad', max_length=40, blank=True)

    class meta:
        verbose_name = 'Planta Principal'
        verbose_name_plural = 'Plantas Principales'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class PlantaSecundaria(models.Model):
    nombre = models.CharField('Planta', max_length=70, blank=False)
    codigo = models.CharField('Código', max_length=10, blank=False)
    descripcion = models.CharField('Descripción', max_length=70, blank=True)
    capacidad = models.CharField('Capacidad', max_length=40, blank=True)

    class meta:
        verbose_name = 'Planta Secundaria'
        verbose_name_plural = 'Plantas Secundarias'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


#SISTEMAS
class Sistema(models.Model):
    nombre = models.CharField('Sistema', max_length=70, blank=False)
    codigo = models.CharField('Código', max_length=10, blank=False)
    descripcion = models.CharField('Descripción', max_length=70, blank=True)
    #planta = models.ManyToManyField(Planta)
    class meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class SubSistema(models.Model):
    nombre = models.CharField('Sistema', max_length=70, blank=False)
    codigo = models.CharField('Código', max_length=10, blank=False)
    descripcion = models.CharField('Descripción', max_length=70, blank=True)
    #planta = models.ManyToManyField(Planta)
    class meta:
        verbose_name = 'Sub-Sistema'
        verbose_name_plural = 'Sub-Sistemas'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

#ACTIVOS
def validate_file_extension(datasheet):
  import os
  ext = os.path.splitext(datasheet.name)[1]
  valid_extensions = ['.pdf']
  if not ext in valid_extensions:
    raise ValidationError(u'Formato de archivo no válido. Seleccione un archivo de extensión ".pdf"')

class EquipoPrincipal(models.Model):
    #numero = models.IntegerField('Número')
    planta = models.ForeignKey(Planta,on_delete=models.CASCADE)
    planta_secundaria = models.ForeignKey(PlantaSecundaria,on_delete=models.CASCADE)
    sistema = models.ForeignKey(Sistema,on_delete=models.CASCADE)
    subsistema =models.ForeignKey(SubSistema,on_delete=models.CASCADE,blank=True,default='---')
    codigo = models.CharField('Código', max_length=10, blank=False)
    nombre = models.CharField('Descripción', max_length=70, blank=False)
    codes=models.CharField(max_length=70,blank=True,default='????')
    marca = models.CharField('Marca', max_length=20, blank=True)
    modelo = models.CharField('Modelo', max_length=20, blank=True)
    serie = models.CharField('Serie', max_length=20, blank=True)    
    tipo = models.CharField('Tipo', max_length=20, blank=True)
    codigo_de_activo= models.CharField('Código de activo', max_length=20, blank=True)
    año = models.DateField('Fecha de instalación',blank=True,null=True)
    capacidad = models.CharField('Capacidad de Diseño/Operativa', max_length=70, blank=True)
    potencia= models.CharField('Potencia', max_length=20, blank=True)
    presion = models.CharField('Presión descarga', max_length=20, blank=True)
    producto = models.CharField('Producto', max_length=20, blank=True)
    temperatura = models.CharField('Temperatura', max_length=20, blank=True)
    voltaje = models.CharField('Voltaje', max_length=20, blank=True)
    fases = models.CharField('Nro. de Fases', max_length=20, blank=True)
    datasheet = models.FileField('Datasheet',upload_to='',validators=[validate_file_extension], blank=True,null=True)
    fu_mantenimiento = models.DateField('Fecha de último mantenimiento integral',blank=True,null=True)
    estado = models.CharField('Estado Operativo', max_length=9, choices=ESTADO, default='O')
    observaciones = models.CharField('Observaciones', max_length=100, blank=True)
    ingresado = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modificado = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Equipo Principal'
       verbose_name_plural = 'Equipos Principales'
       ordering = ['codigo']
    
    def __str__(self):
        cadena=self.codigo+" --- "+self.nombre +" --- "+self.capacidad
        return cadena

    def estado_operativo(self):
        if self.estado == 'O':
            # return format_html('<span style="background:green;">'+self.estado+'</span>')
            return format_html('<span style="background:green;">OPERATIVO (O)</span>')
        else:
            return format_html('<span style="background:red;">FUERA DE SERVICIO (F)</span>')


    @property
    def codigo_total(self):
        return (self.planta.nombre+' - '+self.planta_secundaria.nombre+' - '+self.sistema.nombre+' - '+self.subsistema.nombre)

    def save(self):
        self.codes = self.codigo_total
        super (EquipoPrincipal, self).save()


class Equipo(models.Model):
    #numero = models.IntegerField('Número')
    planta = models.ForeignKey(Planta,on_delete=models.CASCADE)
    planta_secundaria = models.ForeignKey(PlantaSecundaria,on_delete=models.CASCADE)
    sistema = models.ForeignKey(Sistema,on_delete=models.CASCADE)
    subsistema =models.ForeignKey(SubSistema,on_delete=models.CASCADE,blank=True,default='---')
    equipo_principal = models.ForeignKey(EquipoPrincipal,on_delete=models.CASCADE)
    codigo = models.CharField('Código', max_length=10, blank=False)
    nombre = models.CharField('Descripción', max_length=70, blank=False)
    codes=models.CharField(max_length=70,blank=True,default='????')
    marca = models.CharField('Marca', max_length=20, blank=True)
    modelo = models.CharField('Modelo', max_length=20, blank=True)
    serie = models.CharField('Serie', max_length=20, blank=True)    
    tipo = models.CharField('Tipo', max_length=20, blank=True)
    codigo_de_activo= models.CharField('Código de activo', max_length=20, blank=True)
    año = models.DateField('Fecha de instalación',blank=True,null=True)
    capacidad = models.CharField('Capacidad de Diseño/Operativa', max_length=70, blank=True)
    potencia= models.CharField('Potencia', max_length=20, blank=True)
    presion = models.CharField('Presión descarga', max_length=20, blank=True)
    producto = models.CharField('Producto', max_length=20, blank=True)
    temperatura = models.CharField('Temperatura', max_length=20, blank=True)
    voltaje = models.CharField('Voltaje', max_length=20, blank=True)
    fases = models.CharField('Nro. de Fases', max_length=20, blank=True)
    datasheet = models.FileField('Datasheet',upload_to='',validators=[validate_file_extension], blank=True,null=True)
    fu_mantenimiento = models.DateField('Fecha de último mantenimiento integral',blank=True,null=True)
    estado = models.CharField('Estado Operativo', max_length=9, choices=ESTADO, default='O')
    observaciones = models.CharField('Observaciones', max_length=100, blank=True)
    ingresado = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modificado = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Equipo Secuandario'
       verbose_name_plural = 'Equipos Secundarios'
       ordering = ['codigo']
    
    def __str__(self):
        cadena=self.codigo+" --- "+self.nombre +" --- "+self.capacidad
        return cadena

    def estado_operativo(self):
        if self.estado == 'O':
            # return format_html('<span style="background:green;">'+self.estado+'</span>')
            return format_html('<span style="background:green;">OPERATIVO (O)</span>')
        else:
            return format_html('<span style="background:red;">FUERA DE SERVICIO (F)</span>')


    @property
    def codigo_total(self):
        return (self.planta.nombre+' - '+self.planta_secundaria.nombre+' - '+self.sistema.nombre+' - '+self.subsistema.nombre+' - '+self.equipo_principal.nombre)

    def save(self):
        self.codes = self.codigo_total
        super (Equipo, self).save()
