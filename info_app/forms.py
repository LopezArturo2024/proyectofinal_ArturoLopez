from django import forms

class ClienteForms(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    pais=forms.CharField()
    telefono=forms.IntegerField()
    email=forms.EmailField()
    segmento=forms.CharField()

class EmpleadoForms(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    cargo=forms.CharField()
    telefono=forms.IntegerField()
    email=forms.EmailField()
    fecha_contrato=forms.DateField()

class ProductoForms(forms.Form):
    nombre=forms.CharField()
    categoria=forms.CharField()
    precio=forms.FloatField()
    descripcion=forms.CharField()
    

class VentaForms(forms.Form):
    fecha_venta=forms.DateField()
    cliente=forms.CharField()
    empleado=forms.CharField()
    total=forms.FloatField()

class InventarioForms(forms.Form):
    fecha_inventario=forms.DateField()
    producto=forms.CharField()
    cantidad=forms.IntegerField()