from django.db import models

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return self.name
