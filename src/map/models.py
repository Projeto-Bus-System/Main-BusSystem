from django.db import models
from driver.models import Driver

class Bookmarks(models.Model):
    lat = models.CharField(max_length=15, null=False, blank=False)
    long = models.CharField(max_length=15, null=False, blank=False)
    status_driver = models.BooleanField(default=False)
    name_point = models.CharField(max_length=10, null=False, blank=False)


class Map(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    bookmarks = models.ForeignKey(Bookmarks, on_delete=models.CASCADE)