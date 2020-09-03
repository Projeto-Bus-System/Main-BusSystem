from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    BUS_CHOICES = [
        ["Del", "Del"],
        ["Jaime", "Jaime"],
        ["Ribamar", "Ribamar"]
    ]
    bus = models.CharField(max_length=20, null=False, blank=False, choices=BUS_CHOICES)
    driver_id = models.OneToOneField(User, on_delete=models.CASCADE)