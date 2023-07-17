from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Profile

class UserForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        # Validaciones personalizadas
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if username and len(username) < 3:
            self.add_error('username', 'El nombre de usuario debe tener al menos 3 caracteres.')

        if password1 and len(password1) < 8:
            self.add_error('password1', 'La contraseña debe tener al menos 8 caracteres.')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Las contraseñas no coinciden.')


class UserFormEdit(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')
