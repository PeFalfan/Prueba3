from django.urls import path, include
from django.urls.resolvers import URLPattern
from .import views

URLPattern = [
    path('', views.vista)
]