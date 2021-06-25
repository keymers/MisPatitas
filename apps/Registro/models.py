from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    numero = models.IntegerField()
    contrasena = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    Usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    peso = models.IntegerField()
    estatura = models.FloatField()
    edad = models.IntegerField()
    especie = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    consulta = models.TextField()

    def __str__(self):
        return self.nombre
