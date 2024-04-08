import datetime
from django.db import models

class Type(models.Model):
    name=models.models.CharField( max_length=150, verbose_name='nombres')
    
    def __Srt_(self):
        return self.name

    class Meta:
        verbose_name='type'
        verbose_name_plural='types'
        ordering=['id']

# Create your models here.
class Employee (models.Model):
    type=models.ForeignKey(Type, on_delete=models.CASCADE)
    names=models.models.CharField( max_length=150, verbose_name='nombres empleado')
    dni=models.CharField(max_length=10,unique=True, verbose_name='DNI')
    data_jonined=models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creacion=models.DateField(auto_now=True)
    date_updated=models.DateField(auto_now_add=True)
    age=models.PositiveBigIntegerField(default=0)
    salary=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    avatar=models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae=models.FileField(upload_to='avatar/%Y/%m/%d',null=True, blank=True)

    def __Srt_(self):
        return self.names

    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        ordering=['id']