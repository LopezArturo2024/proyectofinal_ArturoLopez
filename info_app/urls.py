from django.contrib import admin
from django.urls import path
from info_app.views import clientes,empleados,productos,ventas,inventario,inicio,forms_cliente,forms_empleado,forms_producto,forms_venta,forms_inventario

urlpatterns = [
    path('portada/',inicio,name="inicio"),
    path('clientes/',clientes,name="clientes"),
    path('empleados/',empleados,name="empleados"),
    path('productos/',productos,name="productos"),
    path('ventas/',ventas,name="ventas"),
    path('inventario/',inventario,name="inventario"),
    path('formulario_cliente/',forms_cliente,name="formulario_cliente"),
    path('formulario_empleado/',forms_empleado,name="formulario_empleado"),
    path('formulario_producto/',forms_producto,name="formulario_producto"),
    path('formulario_venta/',forms_venta,name="formulario_venta"),
    path('formulario_inventario/',forms_inventario,name="formulario_inventario")
]