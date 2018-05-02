# coding: utf-8

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models


class CustomUser(AbstractBaseUser):
    new_field = models.CharField(max_length=25)
    objects = BaseUserManager()

    USERNAME_FIELD = 'new_field'

class CarManager(models.Manager):
    def create_new(self, owner, brand, car_model, year, price):
        new_car = Car.objects.create(owner=owner, brand=brand, car_model=car_model, year=year, price=price)
        new_car.save()
        return new_car


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=30, db_index=True)
    car_model = models.CharField(max_length=30, db_index=True)
    year = models.IntegerField()
    price = models.IntegerField()

    objects = CarManager()
    def __unicode__(self):
        return "Brand: {0} Model: {1}".format(self.brand, self.car_model)


