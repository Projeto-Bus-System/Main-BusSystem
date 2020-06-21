from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    
    #matricula, ponto, telefone_responsavel, telefone
    matricula = models.CharField(max_length=20, null=False, blank=False)