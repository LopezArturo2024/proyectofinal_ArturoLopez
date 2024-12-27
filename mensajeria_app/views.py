from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from mensajeria_app.models import Mensajeria

# Create your views here.

@login_required(login_url='login')
def enviar_mensaje(request):
    if request.method == "POST":
        destinatario_username=request.POST.get("destinatario")
        contenido=request.POST.get("contenido")
        user_destino=User.objects.get(username=destinatario_username)
        Mensajeria.objects.create(remitente=request.user,destinatario=user_destino,contenido=contenido)
        messages.success(request,f"Se ha enviado el mensaje de forma correcta")
        return redirect("mostrar_mensaje")
    usuarios=User.objects.exclude(username=request.user.username)
    return render(request,'mensajeria_app/enviar_mensaje.html',{"usuarios":usuarios})


@login_required(login_url='login')
def mostrar_mensaje(request):
    mensajes=Mensajeria.objects.filter(destinatario=request.user)
    return render(request,'mensajeria_app/mostrar_mensaje.html',{"mensajes":mensajes})


@login_required(login_url='login')
def ver_mensaje(request,id):
    mensaje=Mensajeria.objects.get(id=id)
    contexto=Mensajeria(remitente=mensaje.remitente,destinatario=mensaje.destinatario,fecha_envio=mensaje.fecha_envio,contenido=mensaje.contenido)
    return render(request,"mensajeria_app/ver_contenido.html",{"contexto":contexto})