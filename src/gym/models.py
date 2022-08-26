from django.db import models

class Actividades(models.Model):
    nombre = models.CharField(max_length=30)
    dia = models.CharField(max_length=30)
    horario = models.IntegerField(default=18)
    cupo = models.IntegerField(default=15)
    class Meta:
        verbose_name = "Actividades"
        verbose_name_plural = "Actividades"

    def __str__(self):
        return f"'Nombre: '{self.nombre}" 

class Socios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null= True)
    cuota_paga = models.BooleanField()

    class Meta:
        verbose_name = "Socios"
        verbose_name_plural = "Socios"

    def __str__(self):
        return f"'Nombre: '{self.nombre} - 'Apellido: '{self.apellido}" 

class Planes(models.Model):
    nombre = models.CharField(max_length=30)
    cantidad_clases = models.IntegerField(default=30)
    precio = models.IntegerField()

    class Meta:
        verbose_name = "Planes"
        verbose_name_plural = "Planes"

    def __str__(self):
        return f"'Nombre: '{self.nombre}"
