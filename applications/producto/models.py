from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = RichTextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    img_principal = models.ImageField(upload_to='productos', null=True, blank=True, verbose_name='Imagen principal')
    personalizable = models.BooleanField(default=False, verbose_name='¿Es personalizable?')
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)
#se agrega la fecha de creacion del producto con posibilidad de guardar una fecha de modificación

    def __str__(self):
        return f"{self.nombre} | Categoria: {self.categoria}"

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']


class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to='productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')

    def __str__(self):
        return f"{self.imagen} | Producto = {self.producto.nombre}"


