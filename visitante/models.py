from django.db import models
from django.utils import timezone
from django.urls import reverse
from jsignature.fields import JSignatureField

# Create your models here.



class Instituciones(models.Model):
    Tipo = (('institucion','institucion'), 
            ('proveedor', 'proveedor')
            )
    nombre              =models.CharField(max_length = 100)
    tipo                =models.CharField(max_length=50, choices= Tipo)
    autorizador         =models.CharField(max_length = 100)
    email_autorizador   =models.EmailField(max_length = 100)
    Tel_autorizador     =models.CharField(max_length = 10) 

    def get_absolute_url(self):
        return reverse('visita-create')

    def __str__(self):
        return self.nombre 


class Visitante(models.Model):
    nombre              = models.CharField(max_length = 50)
    apellido            = models.CharField(max_length = 50)
    cedula              = models.CharField(max_length = 11)
    institucion         = models.ForeignKey(Instituciones,  on_delete=models.CASCADE )
    posicion            = models.CharField(max_length = 100)
    email               = models.EmailField(max_length = 100)
    direccion           = models.TextField()
    celular             = models.CharField(max_length = 10)
    motivo              = models.TextField()
    hora                = models.TimeField()
    fecha               = models.DateField(default=timezone.now)
    entrada             = models.BooleanField(default =False, null =True)
    salida              = models.BooleanField(default =False, null = True)
    hora_entrada        = models.TimeField(blank=True,  null=True)
    hora_salida         = models.TimeField(blank=True,  null=True) 
    duracion            = models.CharField(blank=True, max_length = 10)
    firma_entrada       = JSignatureField(blank = True, null = True)  
    firma_salida        = JSignatureField(blank = True, null = True) 


    class Meta:
        ordering = ["fecha"]


    def get_absolute_url(self):
        return reverse('visita-detail', kwargs={'pk': self.pk})
    # def __str__(self):
    #     return self.institucion 

    def __str__(self):
        return str(self.institucion) + " " + str(self.fecha)

    
class Acompanante(models.Model):
    nombre              = models.CharField(max_length = 50)
    apellido            = models.CharField(max_length = 50)
    cedula              = models.CharField(max_length = 50)
    posicion            = models.CharField(max_length = 50)
    celular             = models.CharField(max_length = 10)
    visita              = models.ForeignKey(Visitante,  on_delete=models.CASCADE )         

    # def get_absolute_url(self):
    #     return reverse('acompanate-create', kwargs={'pk': self.pk})
    def get_absolute_url(self):
        return reverse('visita-detail',kwargs={'pk': self.pk}) 

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido)



    
   