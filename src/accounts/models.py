from django.db import models



class Student(models.Model):
    matricula = models.CharField(max_length=11, null=False, blank=False)
    ponto = models.CharField(max_length=150, null=False, blank=False),
    telefone = models.CharField(max_length=12, null=False, blank=False),
    telefone_responsavel = models.CharField(max_length=12, null=False, blank=False),



class Driver(models.Model):
    onibus = models.CharField(max_length=11, null=False, blank=False)
    pontos =  models.CharField(max_length=1000, null=False, blank=False),
    possou_ponto = models.BooleanField(default=False),
