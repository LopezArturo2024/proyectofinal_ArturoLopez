from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mensajeria(models.Model):
    remitente=models.ForeignKey(User,related_name='mensaje_enviado',on_delete=models.CASCADE)
    destinatario=models.ForeignKey(User,related_name='mensaje_recibido',on_delete=models.CASCADE)
    contenido=models.TextField()
    fecha_envio=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.remitente} a {self.destinatario}"

