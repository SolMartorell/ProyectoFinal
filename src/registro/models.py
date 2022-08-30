
from django.db import models
from django.contrib.auth.models import User




class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.CharField(max_length=300)

    def __str__(self):
        return f"Mensaje de: {self.nombre}"
    