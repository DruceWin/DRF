from django.db import models


class Auto(models.Model):
    brand = models.CharField(max_length=255)
    price = models.IntegerField()
