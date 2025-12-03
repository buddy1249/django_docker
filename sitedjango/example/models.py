from django.db import models

# Create your models here.

from django.db import models

class Agnks(models.Model):
    date = models.CharField(max_length=255, blank=True, default='')
    name = models.CharField(max_length=255)
    waybill = models.CharField(max_length=255)
    amount = models.FloatField()
    column = models.CharField(max_length=255)
    note = models.CharField(max_length=255)

    def __str__(self):
        return self.note