# coding: utf-8

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models


class CustomUser(AbstractBaseUser):
    new_field = models.CharField(max_length=25)
    objects = BaseUserManager()

    USERNAME_FIELD = 'new_field'


class CarManager(models.Manager):
    def create_new(self, owner, make, car_model, year, price, body_type, kilometres, reg_expirity, reg_number, transmission,
                   train, fuel_type, color, equipment, description, state, postcode):
        new_car = Car.objects.create(owner=owner,
                                     make=make,
                                     car_model=car_model,
                                     year=year,
                                     price=price,
                                     body_type=body_type,
                                     kilometres=kilometres,
                                     reg_expirity=reg_expirity,
                                     reg_number=reg_number,
                                     transmission=transmission,
                                     train=train,
                                     fuel_type=fuel_type,
                                     color=color,
                                     equipment=equipment,
                                     description=description,
                                     state=state,
                                     postcode=postcode
                                     )
        new_car.save()
        return new_car


class Car(models.Model):

    BODY_TYPE_CHOICES = (
        ('s', 'Sedan'),
        ('c', 'Coupe'),
        ('h', 'Hatch'),
        ('w', 'Wagon'),
        ('su', 'SUV'),
        ('u', 'Ute'),
        ('m', 'Mini van'),
        ('ca', 'Cabriolet')
    )

    TRANSMISSION_CHOICES = (
        ('a', 'Automatic drive'),
        ('m', 'Manual')
    )

    TRAIN_CHOICES = (
        ('a', 'All Wheel Drive'),
        ('f', 'Forward Wheel Drive'),
        ('r', 'Rear Wheel Drive')
    )

    FUEL_CHOICES = (
        ('p', 'Petrol'),
        ('d', 'Diesel'),
        ('e', 'Electric'),
        ('pe', 'Petrol-Electric'),
        ('pl', 'Petrol/LPG Autogas'),
        ('l', 'LPG Autogas')
    )

    STATE_CHOICES = (
        ('nsw', 'New South Wales'),
        ('qld', 'Queensland'),
        ('sa', 'South Australia'),
        ('tas', 'Tasmania'),
        ('vic', 'Victoria'),
        ('wa', 'Western Australia')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=30, db_index=True)
    car_model = models.CharField(max_length=30, db_index=True)
    body_type = models.CharField(max_length=2, choices=BODY_TYPE_CHOICES)
    year = models.PositiveSmallIntegerField(db_index=True)
    kilometres = models.PositiveIntegerField(db_index=True)
    reg_expirity = models.DateField()
    reg_number = models.CharField(max_length=10)
    transmission = models.CharField(max_length=1, choices=TRANSMISSION_CHOICES)
    train = models.CharField(max_length=1, choices=TRAIN_CHOICES)
    fuel_type = models.CharField(max_length=2, choices=FUEL_CHOICES)
    color = models.CharField(max_length=20, default='white')
    equipment = models.TextField(max_length=255, blank=True, null=True)

    price = models.PositiveIntegerField(db_index=True)
    description = models.TextField(max_length=255, blank=True, null=True)

    state = models.CharField(max_length=3, choices=STATE_CHOICES, null=True, blank=True)
    postcode = models.PositiveSmallIntegerField(null=True, blank=True)

    objects = CarManager()

    def __unicode__(self):
        return "Brand: {0} Model: {1}".format(self.make, self.car_model)

    def __str__(self):
        return str(self.make + " " + self.car_model)


class CarMake(models.Model):
    make = models.CharField(max_length=30)

    def __str__(self):
        return self.make



class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=30)

    def __str__(self):
        return self.car_model


