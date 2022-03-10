from django.db import models
from registro.models import *
# Create your models here.

#OPCIONES
ESTADO = [
    (1,'SI'),
    (0,'NO'),
]
#CRITICIDAD SIMPLE PARA ACTIVOS PRINCIPALES
class CriticidadPr(models.Model):
    activo = models.OneToOneField(EquipoPrincipal,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70,blank=True,default='????') 
    po = models.PositiveIntegerField('¿ES PARTE DE UN PROCESO OPERATIVO PRINCIPAL?',choices=ESTADO, default=0, blank=False)
    ps=models.PositiveIntegerField('¿ES PARTE DE UN SISTEMA?',choices=ESTADO, default=0, blank=False)
    fua = models.PositiveIntegerField('¿SE HA PRODUCIDO ALGUNA FALLA EN EL ÚLTIMO AÑO?',choices=ESTADO, default=0, blank=False)
    pe = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN ECONÓMICA?',choices=ESTADO, default=0, blank=False)
    sh = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN A LA SALUD DEL PERSONAL?',choices=ESTADO, default=0, blank=False)
    ma = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN AL MEDIO AMBIENTE?',choices=ESTADO, default=0, blank=False)
    r = models.PositiveIntegerField('REDUNDANCIA', choices=ESTADO, default=0, blank=False)
    crit_pacial = models.FloatField('CRITICIDAD PARCIAL',blank=False,default=0.00)
    eval_redun = models.PositiveIntegerField('EVAL REDUNDANCIA',blank=False,default=0.00)
    crit_total = models.FloatField('CRITICIDAD TOTAL',blank=False, default=0.00)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Criticidad (Principal)'
       verbose_name_plural = 'Criticidades'
       
    # def __str__(self):
    #      return self.activo
    

    @property
    def CT(self):
        return ((self.po*20)+(self.ps*15)+(self.fua*5)+(self.pe*10)+(self.sh*10)+(self.ma*10))

    def save(self):
        if self.r==1:
            self.eval_redun=0
        if self.r==0:
            self.eval_redun=30       
        self.crit_pacial=self.CT
        self.crit_total=(self.crit_pacial+self.eval_redun)*0.05
        self.nombre=self.activo.nombre+' ('+self.activo.codigo+')'
        super (CriticidadPr, self).save()
    def CTT(self):
        return (self.crit_total)
    def estado(self):
        if self.crit_total >= 0 and self.crit_total<2:
            return format_html('<span style="background:green;"><b>BAJO</span>')
            # return format_html('<span style="background:green;">'+str(self.crit_total)+'</span>')
        if self.crit_total >= 2 and self.crit_total<4:
            return format_html('<span style="background:yellow;color:blue"><b>MEDIO</span>')
        if self.crit_total >= 4 and self.crit_total<=5:
            return format_html('<span style="background:red;"><b>ALTO</span>')

#CRITICIDAD SIMPLE PARA ACTIVOS SECUNDARIOS
class Criticidad(models.Model):
    activo = models.OneToOneField(Equipo,on_delete=models.CASCADE,blank=True)  
    nombre=models.CharField(max_length=70,blank=True,default='????')
    po = models.PositiveIntegerField('¿ES PARTE DE UN PROCESO OPERATIVO PRINCIPAL?',choices=ESTADO, default=0, blank=False)
    ps=models.PositiveIntegerField('¿ES PARTE DE UN SISTEMA?',choices=ESTADO, default=0, blank=False)
    fua = models.PositiveIntegerField('¿SE HA PRODUCIDO ALGUNA FALLA EN EL ÚLTIMO AÑO?',choices=ESTADO, default=0, blank=False)
    pe = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN ECONÓMICA?',choices=ESTADO, default=0, blank=False)
    sh = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN A LA SALUD DEL PERSONAL?',choices=ESTADO, default=0, blank=False)
    ma = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN AL MEDIO AMBIENTE?',choices=ESTADO, default=0, blank=False)
    r = models.PositiveIntegerField('REDUNDANCIA', choices=ESTADO, default=0, blank=False)
    crit_pacial = models.FloatField('CRITICIDAD PARCIAL',blank=False,default=0.00)
    eval_redun = models.PositiveIntegerField('EVAL REDUNDANCIA',blank=False,default=0.00)
    crit_total = models.FloatField('CRITICIDAD TOTAL',blank=False, default=0.00)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Criticidad (Secundaria)'
       verbose_name_plural = 'Criticidades'
       
    # def __str__(self):
    #      return self.activo
    

    @property
    def CT(self):
        return ((self.po*20)+(self.ps*15)+(self.fua*5)+(self.pe*10)+(self.sh*10)+(self.ma*10))

    def save(self):
        if self.r==1:
            self.eval_redun=0
        if self.r==0:
            self.eval_redun=30       
        self.crit_pacial=self.CT
        self.crit_total=(self.crit_pacial+self.eval_redun)*0.05
        self.nombre=self.activo.nombre+' ('+self.activo.codigo+')'
        super (Criticidad, self).save()
    def CTT(self):
        return (self.crit_total)
    def estado(self):
        if self.crit_total >= 0 and self.crit_total<2:
            return format_html('<span style="background:green;"><b>BAJO</span>')
            # return format_html('<span style="background:green;">'+str(self.crit_total)+'</span>')
        if self.crit_total >= 2 and self.crit_total<4:
            return format_html('<span style="background:yellow;color:blue"><b>MEDIO</span>')
        if self.crit_total >= 4 and self.crit_total<=5:
            return format_html('<span style="background:red;"><b>ALTO</span>')

#FORMULARIOS DE VALORES PARA CÁLCULO DE LA CRITICIDAD

class Redundancia(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class Ocurrencia(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class Segysa(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class MdA(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class Costo(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class Perdida(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class Exposicion(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

# VALORES DE RANGOS (INTOLERABLE, ALTO, MEDIO...)
# class CategoriaRiesgo(models.Model):
#     intolerable = models.PositiveIntegerField(default=400, blank=False)
#     alto = models.PositiveIntegerField(default=200, blank=False)
#     medio = models.PositiveIntegerField(default=70, blank=False)
#     moderado = models.PositiveIntegerField(default=20, blank=False)

#     def __str__(self):
#         return ('Categoría '+self.id)


#CRITICIDAD COMPLETA PARA ACTIVOS PRINCIPALES

class CriticidadCPr(models.Model):
    tag= models.CharField(max_length=30,blank=True)
    activo = models.OneToOneField(EquipoPrincipal,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=70,blank=True,default='????')
    locacion = models.CharField('LOCACIÓN',max_length=70,blank=True) 
    r = models.ForeignKey(Redundancia,on_delete=models.CASCADE)
    fallas=models.PositiveIntegerField('NÚMERO DE FALLAS', default=0, blank=True)
    mtbf = models.PositiveIntegerField('MTBF', default=0, blank=True)
    ocurrencia = models.ForeignKey(Ocurrencia,on_delete=models.CASCADE)
    segysa = models.ForeignKey(Segysa,on_delete=models.CASCADE)
    md = models.ForeignKey(MdA,on_delete=models.CASCADE)
    cm = models.ForeignKey(Costo,on_delete=models.CASCADE)
    pp = models.ForeignKey(Perdida,on_delete=models.CASCADE)
    ex= models.ForeignKey(Exposicion,on_delete=models.CASCADE)
    vdr = models.PositiveIntegerField('VALOR DE RIESGO',blank=True,default=0)
    ctdr = models.CharField('CATEGORÍA DE RIESGO',max_length=30,blank=True,default='???')
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Criticidad (Principal)'
       verbose_name_plural = 'Criticidades'
       
    # def __str__(self):
    #      return self.activo
    
    #OCURRENCIA*EXPOSICIÓN*SUMA()
    @property
    def VDR(self):
       return ((self.ocurrencia.valor)*(self.ex.valor)*((self.segysa.valor)+(self.md.valor)+(self.cm.valor)+(self.pp.valor)+(self.r.valor)))
    def save(self):
        self.locacion=self.activo.planta.nombre
        self.nombre=self.activo.nombre+' ('+self.activo.codigo+')'+' - '+self.locacion
        self.tag=self.activo.codigo
        self.vdr=self.VDR
        if self.vdr>400:
            self.ctdr='INTOLERABLE'
        if self.vdr>200 and self.vdr<=400:
            self.ctdr='ALTO'
        if self.vdr>70 and self.vdr<=200:
            self.ctdr='MEDIO'
        if self.vdr>20 and self.vdr<=70:
            self.ctdr='MODERADO'
        if self.vdr<=20:
            self.ctdr='ACEPTABLE'
        super (CriticidadCPr, self).save()


#CRITICIDAD COMPLETA PARA ACTIVOS SECUNDARIOS

class CriticidadCSec(models.Model):
    tag= models.CharField(max_length=30,blank=True)
    activo = models.OneToOneField(Equipo,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=70,blank=True,default='????')    
    locacion = models.CharField('LOCACIÓN',max_length=70,blank=True) 
    r = models.ForeignKey(Redundancia,on_delete=models.CASCADE)
    fallas=models.PositiveIntegerField('NÚMERO DE FALLAS', default=0, blank=True)
    mtbf = models.PositiveIntegerField('MTBF', default=0, blank=True)
    ocurrencia = models.ForeignKey(Ocurrencia,on_delete=models.CASCADE)
    segysa = models.ForeignKey(Segysa,on_delete=models.CASCADE)
    md = models.ForeignKey(MdA,on_delete=models.CASCADE)
    cm = models.ForeignKey(Costo,on_delete=models.CASCADE)
    pp = models.ForeignKey(Perdida,on_delete=models.CASCADE)
    ex= models.ForeignKey(Exposicion,on_delete=models.CASCADE)
    vdr = models.PositiveIntegerField('VALOR DE RIESGO',blank=False,default=0)
    ctdr = models.CharField('CATEGORÍA DE RIESGO',max_length=30,blank=True)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Criticidad (Secundaria)'
       verbose_name_plural = 'Criticidades'
       
    # def __str__(self):
    #      return self.activo
    
    #OCURRENCIA*EXPOSICIÓN*SUMA()
    @property
    def VDR(self):
       return ((self.ocurrencia.valor)*(self.ex.valor)*((self.segysa.valor)+(self.md.valor)+(self.cm.valor)+(self.pp.valor)+(self.r.valor)))
    def save(self):
        self.locacion=self.activo.planta.nombre
        self.nombre=self.activo.nombre+' ('+self.activo.codigo+')'+' - '+self.locacion
        self.tag=self.activo.codigo
        self.vdr=self.VDR
        if self.vdr>400:
            self.ctdr='INTOLERABLE'
        if self.vdr>200 and self.vdr<=400:
            self.ctdr='ALTO'
        if self.vdr>70 and self.vdr<=200:
            self.ctdr='MEDIO'
        if self.vdr>20 and self.vdr<=70:
            self.ctdr='MODERADO'
        if self.vdr<=20:
            self.ctdr='ACEPTABLE'
        super (CriticidadCSec, self).save()
