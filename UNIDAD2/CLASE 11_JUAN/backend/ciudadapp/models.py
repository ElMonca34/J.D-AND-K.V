from django.db import models

class ciudad(models.Model):
    ciudad = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100)
    area = models.IntegerField()
    pais = models.CharField(max_length=100)

    def _str_(self):
        return f'{self.ciudad} - {self.poblacion} - {self.area} - {self.pais}'