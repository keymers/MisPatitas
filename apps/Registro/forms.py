from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'peso', 'estatura', 'edad', 'especie']

        labels = {
            'nombre': 'Nombre',
            'peso': 'peso',
            'estatura': 'Estatura en cm',
            'edad': 'edad',
            'especie': 'especie',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.TextInput(attrs={'class': 'form-control'}),
            'estatura': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
