from django.db import models



class Student(models.Model):
    matricula = models.Charfield(max_length=11, null=False, blank=False)
    """ponto,
    telefone,
    telefone_responsavel"""


