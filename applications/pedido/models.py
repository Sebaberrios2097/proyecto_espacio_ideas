from django.db import models
from django.contrib.auth.models import User
from applications.producto.models import Producto
from applications.personalizacion.models import Personalizacion

class Pedido(models.Model):
    ESTADOS = (
        ('PENDIENTE', 'Pendiente'),
        ('PROCESADO', 'Procesado'),
        ('ENVIADO', 'Enviado'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    )
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.username}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    mensaje_personalizado = models.TextField(blank=True, null=True)
    personalizacion = models.ForeignKey(Personalizacion, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.producto.nombre} (x{self.cantidad}) - Pedido #{self.pedido.id}'

    class Meta:
        verbose_name = 'Detalle Pedido'
        verbose_name_plural = 'Detalles Pedido'

