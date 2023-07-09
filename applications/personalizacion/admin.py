from django.contrib import admin
from .models import Personalizacion, ImagenPersonalizacion
from django import forms

class ImagenPersonalizacionInline(admin.TabularInline):
    model = ImagenPersonalizacion
    extra = 1
    min_num = 1
    max_num = 10
    fields = ('imagen',)  # Solo muestra el campo 'imagen' en el inline.

class PersonalizacionAdmin(admin.ModelAdmin):
    inlines = [ImagenPersonalizacionInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Establece automáticamente el valor de persoPredefinida como None.
        if db_field.name == "persoPredefinida":
            kwargs['widget'] = forms.HiddenInput()
            kwargs['initial'] = None
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Personalizacion, PersonalizacionAdmin)
