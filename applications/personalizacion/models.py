from django.db import models
from applications.producto.models import Producto
from django.contrib.auth.models import User


class Personalizacion(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    img_perso = models.ImageField(upload_to='personalizacion', blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Personalizacion'
        verbose_name_plural = 'Personalizaciones'