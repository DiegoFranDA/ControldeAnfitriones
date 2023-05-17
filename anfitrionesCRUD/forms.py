from django import forms
from .models import Anfitrion

class AnfitrionForm(forms.ModelForm):
    class Meta:
        model = Anfitrion
        fields = '__all__'  # Importamos todos los campos del modelo Anfitrion


    grado = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Grado de estudio: ',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    nombre = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Tu nombre: ',
        'class': 'w-full py-4 px-6 rounded-xl',
        'required': 'required'
    }))
    paterno = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Apellido paterno',
        'class': 'w-full py-4 px-6 rounded-xl',
        'required': 'required'
    }))
    materno = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Apellido materno',
        'class': 'w-full py-4 px-6 rounded-xl',
        'required': 'required'
    }))
    cargo = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Cargo: ',
        'class': 'w-full py-4 px-6 rounded-xl',
        'required': 'required'
    }))
    dependencia = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Dependencia: ',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    telefono = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Telefono: ',
        'class': 'w-full py-4 px-6 rounded-xl',
        'required': 'required'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email: ',
        'class': 'w-full py-4 px-6 rounded-xl',
        'required': 'required'
    }))
    extension = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Extension: ',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
