from django.db import models

# Create your models here.
class Productos(models.Model):
    Nombre = models.CharField(max_length=100)
    Precio = models.IntegerField()
    Cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.Nombre} {self.precio}"
