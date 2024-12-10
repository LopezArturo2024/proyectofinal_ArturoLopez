from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    pais=models.CharField(max_length=15)
    telefono=models.IntegerField()
    email=models.EmailField()
    segmento=models.CharField(max_length=15)

class Empleado(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    cargo=models.CharField(max_length=20)
    telefono=models.IntegerField()
    email=models.EmailField()
    fecha_contrato=models.DateField()

class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    categoria=models.CharField(max_length=30)
    precio=models.FloatField()
    descripcion=models.CharField(max_length=200)

class Venta(models.Model):
    fecha_venta=models.DateField()
    cliente=models.CharField(max_length=30)
    empleado=models.CharField(max_length=30)
    total=models.FloatField()

class Inventario(models.Model):
    fecha_inventario=models.DateField()
    producto=models.CharField(max_length=100)
    cantidad=models.IntegerField()
