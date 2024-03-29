from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Motocycle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.FloatField()
    concerns = models.ForeignKey('Concern', on_delete=models.CASCADE)
    shops = models.ManyToManyField('Store')

    def __str__(self):
        return self.model


class Concern(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)


class House(models.Model):
    address = models.CharField(max_length=100)
    persons = models.ForeignKey(Person, on_delete=models.CASCADE)
