from django.db import models

class Usuario(models.Model):
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.correo 
