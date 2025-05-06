from django.db import models

class ciudad(models.Model):
    ciudad = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100)
    area = models.IntegerField()
    pais = models.DateField()

    def __str__(self):
        return f'{self.ciudad} - {self.poblacion} - {self.area} - {self.pais}'