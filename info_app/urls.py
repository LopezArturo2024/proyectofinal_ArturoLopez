from django.contrib import admin
from django.urls import path
from info_app.views import clientes,empleados,productos,ventas,inventario,inicio,forms_cliente,forms_empleado,forms_producto,forms_venta,forms_inventario,sobre_mi,user_create,user_login,user_logout,ver_perfil,edit_profile,edit_password,eliminar_cliente,actualizar_cliente,ver_cliente,ver_empleado,actualizar_empleado,eliminar_empleado,ver_productos,eliminar_producto,actualizar_producto

urlpatterns = [
    path('portada/',inicio,name="inicio"),
    path('aboutme/',sobre_mi,name="about"),
    path('clientes/',clientes,name="clientes"),
    path('empleados/',empleados,name="empleados"),
    path('productos/',productos,name="productos"),
    path('ventas/',ventas,name="ventas"),
    path('inventario/',inventario,name="inventario"),

    #Formularios
    path('formulario_cliente/',forms_cliente,name="formulario_cliente"),
    path('formulario_empleado/',forms_empleado,name="formulario_empleado"),
    path('formulario_producto/',forms_producto,name="formulario_producto"),
    path('formulario_venta/',forms_venta,name="formulario_venta"),
    path('formulario_inventario/',forms_inventario,name="formulario_inventario"),

    #User
    path('usercreate/',user_create,name="usercreate"),
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    path('ver_perfil/',ver_perfil,name="ver_perfil"),
    path('editar_perfil/',edit_profile,name="editar_perfil"),
    path('editar_pasword/',edit_password,name="editar_password"),

    #CRUD Clientes
    path('ver_cliente/<int:id>',ver_cliente,name="ver_cliente"),
    path('eliminar_cliente/<int:id>',eliminar_cliente,name="eliminar_cliente"),
    path('editar_cliente/<int:id>',actualizar_cliente,name="editar_cliente"),


    #CRUD Empleados
    path('ver_empleado/<int:id>',ver_empleado,name="ver_empleado"),
    path('eliminar_empleado/<int:id>',eliminar_empleado,name="eliminar_empleado"),
    path('editar_empleado/<int:id>',actualizar_empleado,name="editar_empleado"),

    #CRUD Productos
    path('ver_producto/<int:id>',ver_productos,name="ver_producto"),
    path('eliminar_producto/<int:id>',eliminar_producto,name="eliminar_producto"),
    path('editar_producto/<int:id>',actualizar_producto,name="editar_producto")
]