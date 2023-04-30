from django.contrib import admin
from .models import Producto, Categoria, ImagenProducto

#haz un inline para que se muestre en el mismo formulario de producto
class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    exclude = ['fecha_creacion']
    inlines = [ImagenProductoInline]
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'personalizable', 'fecha_creacion', 'aviso')
    search_fields = ('nombre', 'categoria__nombre', 'fecha_creacion')
    list_filter = ('categoria', 'personalizable', 'fecha_creacion')
    fieldsets = (        
        ('Información del producto', {
            'fields': ('nombre', 'precio', 'stock', 'categoria', 'personalizable')
        }),
        ('Información adicional', {
            'fields': ('descripcion', 'img_principal','aviso' , 'aviso_personalizacion')
        }))


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(ImagenProducto)

