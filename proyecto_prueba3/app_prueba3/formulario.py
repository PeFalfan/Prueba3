from django import forms
from .models import Vehiculo

class NuevoVehiculo (forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('vin', 'patente' ,'anio_fabricacion',
                  'fecha_recepcion' , 'marca' ,'modelo')