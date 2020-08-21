from django.urls import path, include
from accounts.views import render_user

urlpatterns = [
    path('criar-conta/', render_user ,name="CriarConta"),

]