from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.marca} {self.modelo} ({self.año})"
