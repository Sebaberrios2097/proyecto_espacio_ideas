from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

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
    descripcion = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    img_principal = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} | Categoria: {self.categoria}"

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']


class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to='productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    principal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.producto.nombre} | Principal: {self.principal}"


