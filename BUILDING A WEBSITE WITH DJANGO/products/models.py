from sys import modules
from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=225)
    discount = models.FloatField()
