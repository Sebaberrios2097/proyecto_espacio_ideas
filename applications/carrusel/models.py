from django.db import models

# Create your models here.

class Carrusel(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='carrusel')
    encabezado = models.CharField(max_length=50)
    subencabezado = models.CharField(max_length=350)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Carrusel'
        verbose_name_plural = 'Carrusel'
        ordering = ['-fecha_creacion']