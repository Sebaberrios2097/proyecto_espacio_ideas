from django.db import models
<<<<<<< HEAD
from applications.producto.models import Producto
<<<<<<< HEAD
from django.contrib.auth.models import User


class Personalizacion(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
=======

class Personalizacion(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
>>>>>>> Seba
=======

class Personalizacion(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
>>>>>>> Seba
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    # producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Elimina esta línea

<<<<<<< HEAD

=======
>>>>>>> Seba
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Personalizacion'
        verbose_name_plural = 'Personalizaciones'


class ImagenPersonalizacion(models.Model):
    personalizacion = models.ForeignKey(Personalizacion, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='personalizacion', blank=True, null=True)

    def __str__(self):
        return self.personalizacion.nombre

    
    class Meta:
        verbose_name = 'Imagen Personalizacion'
        verbose_name_plural = 'Imagenes Personalizacion'