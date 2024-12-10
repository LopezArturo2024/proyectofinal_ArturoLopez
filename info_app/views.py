from django.shortcuts import render,redirect
from django.db.models import Q
from info_app.models import Cliente,Empleado,Producto,Venta,Inventario
from info_app.forms import ClienteForms,EmpleadoForms,ProductoForms,VentaForms,InventarioForms


# Create your views here.
def inicio(request):
    return render(request,"info_app/portada.html")


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





def forms_cliente(request):
    if request.method == "POST":
        cliente_form=ClienteForms(request.POST)
        if cliente_form.is_valid():
            info_limpia=cliente_form.cleaned_data
            cliente=Cliente(nombre=info_limpia["nombre"],apellido=info_limpia["apellido"],pais=info_limpia["pais"],telefono=info_limpia["telefono"],email=info_limpia["email"],segmento=info_limpia["segmento"])
            cliente.save()
            return redirect("clientes")
    else:
        cliente_form=ClienteForms()
        
    contexto={"forms":cliente_form}
    return render(request,"info_app/forms/clienteForms.html",contexto)



def forms_empleado(request):
    if request.method == "POST":
        empleado_form=EmpleadoForms(request.POST)
        if empleado_form.is_valid():
            info_limpia=empleado_form.cleaned_data
            empleado=Empleado(nombre=info_limpia["nombre"],apellido=info_limpia["apellido"],cargo=info_limpia["cargo"],telefono=info_limpia["telefono"],email=info_limpia["email"],fecha_contrato=info_limpia["fecha_contrato"])
            empleado.save()
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