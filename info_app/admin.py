from django.contrib import admin
from info_app.models import Cliente,Empleado,Producto,Venta,Inventario,Profile

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Inventario)
admin.site.register(Profile)
