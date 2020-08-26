from django.urls import path, include
from accounts.views import createStudent

urlpatterns = [
    path('criar-conta/', createStudent ,name="CriarConta"),

]