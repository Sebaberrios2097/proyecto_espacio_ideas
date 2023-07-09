from django import forms
from .models import Personalizacion, ImagenPersonalizacion

# class PersonalizacionForm(forms.ModelForm):
#     class Meta:
#         model = Personalizacion
#         fields = ['user', 'nombre', 'descripcion', 'fecha', 'activo', 'producto']
#         widgets = {
#             'descripcion': forms.Textarea(attrs={'rows': 3}),
#         }

class PersonalizacionCreateForm(forms.ModelForm):
    class Meta:
        model = Personalizacion
        fields = ['user', 'nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre de la personalización',
            'descripcion': 'Descripción de la personalización',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'resize': 'none'}),
            'user': forms.HiddenInput(),
        }

class ImagenPersonalizacionForm(forms.ModelForm):
    class Meta:
        model = ImagenPersonalizacion
        fields = ['personalizacion', 'imagen']

        # Omitir 'personalizacion' y 'persoPredefinida' si planeas manejarlos automáticamente
        # en función del contexto en el que se utilice el formulario:
        # fields = ['imagen']
