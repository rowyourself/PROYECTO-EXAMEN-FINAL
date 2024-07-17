from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino')], required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'telefono', 'sexo', 'fecha_nacimiento']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            
            # Guardar el perfil de usuario
            UserProfile.objects.create(
                user=user,
                telefono=self.cleaned_data['telefono'],
                sexo=self.cleaned_data['sexo'],
                fecha_nacimiento=self.cleaned_data['fecha_nacimiento']
            )
        return user