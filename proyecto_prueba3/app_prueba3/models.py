from django.db import models
from django.utils import timezone

# Create your models here.
class Vehiculo(models.Model):
    vin = models.CharField(max_length=17)
    patente = models.CharField(max_length=6)
    anio_fabricacion = models.CharField(max_length=4)
    fecha_recepcion = models.DateTimeField(blank=True, null=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.vin + "\n" + self.patente + "\n" + self.anio_fabricacion + "\n" + self.fecha_recepcion + "\n" + self.marca + "\n" + self.modelo


