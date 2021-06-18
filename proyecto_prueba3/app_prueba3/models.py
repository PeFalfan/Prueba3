from django.db import models
from django.utils import timezone

# Create your models here.
class Vehiculo(models.Model):
    vin = models.CharField(max_length=17, blank=False, null=False)
    patente = models.CharField(max_length=6, blank=False, null=False)
    anio_fabricacion = models.DecimalField(max_digits=4, decimal_places=0, blank=False, null=False)
    fecha_recepcion = models.DateTimeField(blank=True, null=True)
    marca = models.CharField(max_length=20, blank=False, null=False)
    modelo = models.CharField(max_length=20, blank=False, null=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def Post(self):
        return self.Post()

    def __str__(self):
        return self.vin + "\n" + self.patente + "\n" + self.marca + "\n" + self.modelo
