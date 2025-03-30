from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    poblacion = models.IntegerField()
    area = models.FloatField()
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre