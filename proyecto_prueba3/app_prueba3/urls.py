from django.db.models import indexes
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index),
    path('proyecto_prueba3/app_prueba3/templates/app_prueba3/vistaVehiculo.html/', views.vistaVehiculo),
    path('proyecto_prueba3/app_prueba3/templates/app_prueba3/nuevoVehiculo.html/', views.nuevoVehiculo),
]