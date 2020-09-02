from django.contrib import admin
from django.urls import path, include
from .views import render_map

urlpatterns = [
    path('', render_map)    
]
