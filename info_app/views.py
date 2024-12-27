from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required

from info_app.models import Cliente,Empleado,Producto,Venta,Inventario,Profile
from info_app.forms import ClienteForms,EmpleadoForms,ProductoForms,VentaForms,InventarioForms,UpdateuserForms,UserphotoForms



# Create your views here.

def inicio(request):
    return render(request,"info_app/portada.html")




def sobre_mi(request):
    return render(request,"info_app/about.html")




@login_required(login_url='login')
def clientes(request):
    query=request.GET.get("q")

    if query:
        cliente=Cliente.objects.filter(Q(nombre__icontains=query) | 
                                        Q(apellido__icontains=query) )
    else:
        cliente=Cliente.objects.all()    

    contexto={"cliente":cliente}
    return render(request,"info_app/clientes.html",contexto)





def empleados(request):
    query=request.GET.get("q")

    if query:
        empleado=Empleado.objects.filter(Q(nombre__icontains=query) | 
                                        Q(apellido__icontains=query) )
    else:
        empleado=Empleado.objects.all()    

    contexto={"empleado":empleado}
    return render(request,"info_app/empleados.html",contexto)
    



def productos(request):
    query=request.GET.get("q")

    if query:
        producto=Producto.objects.filter(Q(nombre__icontains=query) | 
                                        Q(categoria__icontains=query) )
    else:
        producto=Producto.objects.all()    

    contexto={"producto":producto}
    return render(request,"info_app/productos.html",contexto)




def ventas(request):
    query=request.GET.get("q")

    if query:
        venta=Venta.objects.filter(Q(id__icontains=query) | 
                                Q(cliente__icontains=query) )
    else:
        venta=Venta.objects.all()    

    contexto={"venta":venta}
    return render(request,"info_app/ventas.html",contexto)





def inventario(request):
    query=request.GET.get("q")

    if query:
        inventario=Inventario.objects.filter(Q(id__icontains=query) | 
                                            Q(producto__icontains=query))
    else:
        inventario=Inventario.objects.all()    

    contexto={"inventario":inventario}
    return render(request,"info_app/inventario.html",contexto)




@login_required(login_url='login')
def forms_cliente(request):
    if request.method == "POST":
        cliente_form=ClienteForms(request.POST)
        if cliente_form.is_valid():
            info_limpia=cliente_form.cleaned_data
            cliente=Cliente(nombre=info_limpia["nombre"],apellido=info_limpia["apellido"],pais=info_limpia["pais"],telefono=info_limpia["telefono"],email=info_limpia["email"],segmento=info_limpia["segmento"])
            cliente.save()
            messages.success(request,f"Se ha creado el cliente {cliente.nombre} {cliente.apellido} de forma correcta")
            return redirect("clientes")
    else:
        cliente_form=ClienteForms()
        
    contexto={"forms":cliente_form}
    return render(request,"info_app/forms/clienteForms.html",contexto)


@login_required(login_url='login')
def forms_empleado(request):
    if request.method == "POST":
        empleado_form=EmpleadoForms(request.POST)
        if empleado_form.is_valid():
            info_limpia=empleado_form.cleaned_data
            empleado=Empleado(nombre=info_limpia["nombre"],apellido=info_limpia["apellido"],cargo=info_limpia["cargo"],telefono=info_limpia["telefono"],email=info_limpia["email"],fecha_contrato=info_limpia["fecha_contrato"])
            empleado.save()
            messages.success(request,f"Se ha creado el empleado {empleado.nombre} {empleado.apellido} de forma correcta")
            return redirect("empleados")
    else:
        empleado_form=EmpleadoForms()
        
    contexto={"forms":empleado_form}
    return render(request,"info_app/forms/empleadoForms.html",contexto)




def forms_producto(request):
    if request.method == "POST":
        producto_form=ProductoForms(request.POST)
        if producto_form.is_valid():
            info_limpia=producto_form.cleaned_data
            producto=Producto(nombre=info_limpia["nombre"],categoria=info_limpia["categoria"],precio=info_limpia["precio"],descripcion=info_limpia["descripcion"])
            producto.save()
            return redirect("productos")
    else:
        producto_form=ProductoForms()
        
    contexto={"forms":producto_form}
    return render(request,"info_app/forms/productoForms.html",contexto)



def forms_venta(request):
    if request.method == "POST":
        venta_form=VentaForms(request.POST)
        if venta_form.is_valid():
            info_limpia=venta_form.cleaned_data
            venta=Venta(fecha_venta=info_limpia["fecha_venta"],cliente=info_limpia["cliente"],empleado=info_limpia["empleado"],total=info_limpia["total"])
            venta.save()
            return redirect("ventas")
    else:
        venta_form=VentaForms()
        
    contexto={"forms":venta_form}
    return render(request,"info_app/forms/ventaForms.html",contexto)




def forms_inventario(request):
    if request.method == "POST":
        inventario_form=InventarioForms(request.POST)
        if inventario_form.is_valid():
            info_limpia=inventario_form.cleaned_data
            inventario=Inventario(fecha_inventario=info_limpia["fecha_inventario"],producto=info_limpia["producto"],cantidad=info_limpia["cantidad"])
            inventario.save()
            return redirect("inventario")
    else:
        inventario_form=InventarioForms()
        
    contexto={"forms":inventario_form}
    return render(request,"info_app/forms/inventarioForms.html",contexto)



#Ver cliente
@login_required(login_url='login')
def ver_cliente(request,id):
    cliente=Cliente.objects.get(id=id)
    return render(request,"info_app/ver_cliente.html",{"cliente":cliente})

    

#Delete cliente
@login_required(login_url='login')
def eliminar_cliente(request,id):
    cliente=Cliente.objects.get(id=id)
    cliente.delete()
    messages.success(request,f"Se ha eliminado el usuario {cliente.nombre} {cliente.apellido} de forma correcta")
    return redirect('clientes')



#Update cliente
@login_required(login_url='login')
def actualizar_cliente(request,id):
    cliente=Cliente.objects.get(id=id)

    if request.method == "POST":
        cliente_form=ClienteForms(request.POST)
        if cliente_form.is_valid():
            info_limpia=cliente_form.cleaned_data
            cliente.nombre=info_limpia["nombre"]
            cliente.apellido=info_limpia["apellido"]
            cliente.pais=info_limpia["pais"]
            cliente.telefono=info_limpia["telefono"]
            cliente.email=info_limpia["email"]
            cliente.segmento=info_limpia["segmento"]
            cliente.save()
            messages.success(request,f"Se ha actualizado la información del cliente: {cliente.nombre} {cliente.apellido} de forma correcta")
            return redirect('clientes')

    else:
        cliente_form=ClienteForms(initial={"nombre":cliente.nombre,"apellido":cliente.apellido,"pais":cliente.pais,"telefono":cliente.telefono,"email":cliente.email,"segmento":cliente.segmento})
        contexto={"forms":cliente_form}

    return render(request,"info_app/editar_cliente.html",contexto)






#Ver empleado
@login_required(login_url='login')
def ver_empleado(request,id):
    empleado=Empleado.objects.get(id=id)
    return render(request,"info_app/ver_empleado.html",{"empleado":empleado})

    

#Delete cliente
@login_required(login_url='login')
def eliminar_empleado(request,id):
    empleado=Empleado.objects.get(id=id)
    empleado.delete()
    messages.success(request,f"Se ha eliminado el empleado {empleado.nombre} {empleado.apellido} de forma correcta")
    return redirect('empleados')



#Update cliente
@login_required(login_url='login')
def actualizar_empleado(request,id):
    empleado=Empleado.objects.get(id=id)

    if request.method == "POST":
        empleado_form=EmpleadoForms(request.POST)
        if empleado_form.is_valid():
            info_limpia=empleado_form.cleaned_data
            empleado.nombre=info_limpia["nombre"]
            empleado.apellido=info_limpia["apellido"]
            empleado.cargo=info_limpia["cargo"]
            empleado.telefono=info_limpia["telefono"]
            empleado.email=info_limpia["email"]
            empleado.fecha_contrato=info_limpia["fecha_contrato"]
            empleado.save()
            messages.success(request,f"Se ha actualizado la información del empleado: {empleado.nombre} {empleado.apellido} de forma correcta")
            return redirect('empleados')

    else:
        empleado_form=EmpleadoForms(initial={"nombre":empleado.nombre,"apellido":empleado.apellido,"cargo":empleado.cargo,"telefono":empleado.telefono,"email":empleado.email,"fecha_contrato":empleado.fecha_contrato})
        contexto={"forms":empleado_form}

    return render(request,"info_app/editar_empleado.html",contexto)








#Ver Productos
@login_required(login_url='login')
def ver_productos(request,id):
    producto=Producto.objects.get(id=id)
    return render(request,"info_app/ver_producto.html",{"producto":producto})

    

#Delete Producto
@login_required(login_url='login')
def eliminar_producto(request,id):
    producto=Producto.objects.get(id=id)
    producto.delete()
    messages.success(request,f"Se ha eliminado el producto {producto.nombre} de la categoría {producto.categoria} de forma correcta")
    return redirect('productos')



#Update Producto
@login_required(login_url='login')
def actualizar_producto(request,id):
    producto=Producto.objects.get(id=id)

    if request.method == "POST":
        producto_form=ProductoForms(request.POST)
        if producto_form.is_valid():
            info_limpia=producto_form.cleaned_data
            producto.nombre=info_limpia["nombre"]
            producto.categoria=info_limpia["categoria"]
            producto.precio=info_limpia["precio"]
            producto.descripcion=info_limpia["descripcion"]
            producto.save()
            messages.success(request,f"Se ha actualizado la información del producto: {producto.nombre} de la categoría {producto.categoria} de forma correcta")
            return redirect('productos')

    else:
        producto_form=ProductoForms(initial={"nombre":producto.nombre,"categoria":producto.categoria,"precio":producto.precio,"descripcion":producto.descripcion})
        contexto={"forms":producto_form}

    return render(request,"info_app/editar_producto.html",contexto)






































def user_create(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"info_app/mensajes/successuser.html")
        else:
            messages.error(request, "El usuario ya existe o los datos no son válidos")
            return redirect ('usercreate')
    else: 
        form=UserCreationForm()
        contexto={"form":form}
        return render(request,"info_app/forms/createuser.html",contexto)
    


def user_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render (request,"info_app/mensajes/successlogin.html")
        else:
            messages.error(request, "Usuario y/o contraseña no válidos")
            return redirect ('login')
    else:
        return render(request,"info_app/forms/login.html")



def user_logout(request):
    logout(request)
    return redirect ('login')


@login_required(login_url='login')
def ver_perfil(request):
    return render(request,"info_app/perfil.html")


@login_required(login_url='login')
def edit_profile(request):
    usuario = request.user
    perfil,_ = Profile.objects.get_or_create(user=usuario)

    if request.method == "POST":
        forms=UpdateuserForms(request.POST, instance=usuario)
        profile_form=UserphotoForms(request.POST,request.FILES,instance=perfil)

        if forms.is_valid() and profile_form.is_valid():
            forms.save()
            profile_form.save()
            return redirect('ver_perfil')
    else:
        forms=UpdateuserForms(instance=usuario)
        profile_form = UserphotoForms(instance=perfil)

    contexto={"forms":forms,"profile_form":profile_form}
    return render (request,"info_app/forms/editar_perfil.html",contexto)




@login_required(login_url='login')
def edit_password(request):
    usuario = request.user
    if request.method == 'POST':
        forms=PasswordChangeForm(usuario,request.POST)
        if forms.is_valid():
            forms.save()
            update_session_auth_hash(request,usuario)
            messages.success(request,"Contraseña modificada de forma correcta")
            return redirect ('ver_perfil')
    else:
        forms=PasswordChangeForm(usuario)
    return render(request,"info_app/forms/editar_password.html",{"forms":forms})