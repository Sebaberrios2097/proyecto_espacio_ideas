from django import forms
from .models import Producto, Categoria

class CustomProductoCreationForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'descripcion','categoria', 'img_principal', 'personalizable','aviso', 'aviso_personalizacion', 'descripcion_corta']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'style': 'resize:none;'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'img_principal': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'personalizable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'aviso': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'aviso_personalizacion': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'style': 'resize:none;'}),
            'descripcion_corta': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'style': 'resize:none;'}),

        }

class CustomCategoriaCreationForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'style': 'resize:none;'}),
        }