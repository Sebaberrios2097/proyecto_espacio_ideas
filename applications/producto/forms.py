from django import forms
from .models import Producto, Categoria

class CustomProductoCreationForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'descripcion','categoria', 'img_principal']
        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'stock': 'Stock',
            'descripcion': 'Descripción',
            'categoria': 'Categoría',
            'img_principal': 'Imagen principal',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'style': 'resize:none;'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'img_principal': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CustomCategoriaCreationForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'style': 'resize:none;'}),
        }