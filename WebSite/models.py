from django.db import models

# Create your models here.
"""
class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    direccion = models.CharField(max_length=100)
    saldo = models.IntegerField(null=True, default=0)
    hisorial_pagos = models.ManyToManyField("RegistroPago")

    def __str__(self):
        return self.nombre_completo
"""


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='images', null = True)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre
    
"""
class RegistroPago(models.Model):
    fecha_pago = models.DateField(null=True)
    monto_pago = models.IntegerField(default=50000)

    def __str__(self):
        return self.fecha_pago"""