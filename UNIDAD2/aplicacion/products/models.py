from django.db import models # type: ignore

class Products(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.nombre