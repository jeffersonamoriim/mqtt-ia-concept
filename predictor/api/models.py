from django.db import models
from django.db.models.deletion import CASCADE

class Device(models.Model):
    name = models.CharField(max_length=20)
    mac_adress = models.CharField(max_length=20)

class InputData(models.Model):
    value = models.IntegerField()
    type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    device = models.ForeignKey(Device, on_delete=CASCADE)
