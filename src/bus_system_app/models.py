from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    
    telefone_responsavel = models.IntegerField(null=False, blank=False)
    telefone = models.IntegerField(null=False, blank=False)
    ponto = models.CharField(max_length=500, null=False, blank=False)#Os pontos que o aluno geralmente pega (2)
    matricula = models.CharField(max_length=40, null=False, blank=False)
    aluno_usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

class Motorista(models.Model):
    Onibus = models.CharField(max_length=20, null=False, blank=False)
    pontos = models.CharField(max_length=200, null=False, blank=False) #Todos os pontos que o motorista passa(all)
    passou_no_ponto = models.BooleanField(null=False,  default=False)
    motorista_usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
