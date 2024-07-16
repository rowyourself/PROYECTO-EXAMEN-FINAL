from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'contraseña', 'rut', 'nombre', 'telefono', 'fecha_nacimiento']
        widgets = {
            'contraseña': forms.PasswordInput(),  # Campo de contraseña para ocultar el texto
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})  # Widget para seleccionar fecha
        }

class SinginForm(forms.Form):
    correo = forms.EmailField(label='Correo electrónico')
    contraseña = forms.CharField(widget=forms.PasswordInput)