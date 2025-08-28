from django.db import models

# Create your models here.
class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=100)
    precio =  models.FloatField()
    cantidad = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nombre} (${self.precio})"
    