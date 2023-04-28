from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserExtra

class UserForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

class UserFormEdit(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Nombres', widget=forms.TextInput(attrs={'class':'form-control'}))
    user_extra = forms.CharField(widget=forms.HiddenInput(), required=False)
    fono = forms.CharField(label='Teléfono', widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(label='Dirección', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'user_extra')

    def save(self, commit=True):
        user = super().save(commit=False)
        user_extra_data = {
            'fono': self.cleaned_data['fono'],
            'direccion': self.cleaned_data['direccion'],
        }
        if self.cleaned_data['user_extra']:
            user_extra = UserExtra.objects.get(pk=self.cleaned_data['user_extra'])
            user_extra.fono = user_extra_data['fono']
            user_extra.direccion = user_extra_data['direccion']
            user_extra.save()
        else:
            user_extra = UserExtra.objects.create(
                user=user,
                fono=user_extra_data['fono'],
                direccion=user_extra_data['direccion']
            )
            self.cleaned_data['user_extra'] = user_extra.pk

        if commit:
            user.save()
        return user

    
class UserExtraForm(forms.ModelForm):
    fono = forms.CharField(label='Teléfono', widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(label='Dirección', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = UserExtra
        fields = ('fono', 'direccion')