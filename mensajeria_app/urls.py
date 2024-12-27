from django.urls import path
from mensajeria_app.views import mostrar_mensaje,enviar_mensaje,ver_mensaje

urlpatterns = [
    path("mostrar_mensaje/",mostrar_mensaje,name="mostrar_mensaje"),
    path("enviar_mensaje/",enviar_mensaje,name="enviar_mensaje"),
    path("ver_mensaje/<int:id>",ver_mensaje,name="ver_mensaje")
]