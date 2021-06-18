from django.shortcuts import render
from .models import Vehiculo
from .formulario import NuevoVehiculo

# Create your views here.

def index(request):
    return render(request, 'app_prueba3/index.html', {})
    
def vistaVehiculo(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'app_prueba3/vistaVehiculo.html', {'vehiculos': vehiculos})

def nuevoVehiculo(request):
    vehiculo = Vehiculo()

    if request.method == 'POST':
        nuevoVehiculo = NuevoVehiculo(request.POST, instance=vehiculo)          
        nuevoVehiculo.save() 
        return render(request, 'app_prueba3/index.html', {}) 
    else:
        formularioVehiculo = NuevoVehiculo()
        return render(request, 'app_prueba3/nuevoVehiculo.html', {'formularioVehiculo': formularioVehiculo})

    