from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    matricula = models.CharField(max_length=11, null=False, blank=False)
    ponto = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=12, null=False, blank=False)
    telefone_responsavel = models.CharField(max_length=12, null=False, blank=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    