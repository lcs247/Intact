from django.db import models

# Create your models here.

class ConfiabilidadEquipoPr(models.Model):
    activo = models.OneToOneField(EquipoPrincipal,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=70,blank=True,default='????')
    inicio_falla = models.CharField('LOCACIÓN',max_length=70,blank=True) 
    final_falla = models.ForeignKey(Redundancia,on_delete=models.CASCADE)
    uptime=models.PositiveIntegerField('NÚMERO DE FALLAS', default=0, blank=True)
    downtime = models.PositiveIntegerField('MTBF', default=0, blank=True)
    tipo = models.ForeignKey(Ocurrencia,on_delete=models.CASCADE)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)