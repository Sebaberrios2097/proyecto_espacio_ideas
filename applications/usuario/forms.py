from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from .models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
        attrs={
        'class': 'form-control', 
        'placeholder': 'Introduce tu nombre de usuario'}))
    email = forms.EmailField(
        widget=forms.EmailInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'ej. juan.perez@gmail.com'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={
        'class': 'form-control'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={
        'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        password_validation.validate_password(password1, self.instance)
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
