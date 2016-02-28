from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Place(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    time_changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s, %s, %s" %(self.street, self.city, self.state)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    place = models.OneToOneField(Place,
                                 on_delete=models.CASCADE,
                                 primary_key=True)

    serves_hot_dogs = models.BooleanField(default=True)
    serves_pizzas = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

# one waiter can work on many different restaurants
class Waiter(models.Model):
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    restaurant = models.ForeignKey(Restaurant)
    time_created = models.DateTimeField(auto_now_add=True)
    time_changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
