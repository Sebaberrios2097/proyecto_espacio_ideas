from django.db import models
from django.contrib.auth.models import User
from applications.producto.models import Producto, Personalizacion
from django.utils import timezone

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=100, default='Pendiente')
    transaction_id = models.CharField(max_length=100, default=timezone.now().timestamp())
    webpay_token = models.CharField(max_length=200, null=True, blank=True)  # nuevo campo para almacenar el token de Webpay
    
    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.username}'


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    personalizacion = models.ForeignKey(Personalizacion, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(default=1)
    precio = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad} - {self.personalizacion.nombre if self.personalizacion else "Sin personalización"}'
