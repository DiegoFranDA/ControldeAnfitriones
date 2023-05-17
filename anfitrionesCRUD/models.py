from django.db import models

# Create your models here.

class Anfitrion(models.Model):
    idAnfitrion = models.AutoField(primary_key=True)
    grado = models.CharField(max_length=45, null=True)
    nombre = models.CharField(max_length=45, null=True)
    paterno = models.CharField(max_length=45, null=True)
    materno = models.CharField(max_length=45, null=True)
    cargo = models.CharField(max_length=45, null=True)
    dependencia = models.CharField(max_length=255, null=True)
    telefono = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45, null=True)
    extension = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.nombre