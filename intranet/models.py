from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import datetime

#Necesito hacer reservas.

class User(AbstractUser):
    rut = models.CharField(max_length=9, default=12345678)
    birthday = models.DateField("Date", default=datetime.datetime.now())
    GENDER_CHOICES = (('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Otro'))
    gender = models.CharField(max_length=1, default='H', choices=GENDER_CHOICES)


class Service(models.Model):
    id = models.AutoField(db_column='serviceID', primary_key=True)
    name = models.CharField(max_length=64)
    price = models.IntegerField()

    class Meta:
        db_table = 'service'


class Booking(models.Model):
    id = models.AutoField(db_column='bookingID', primary_key=True)
    patente = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'booking'


class CarBookingServices(models.Model):
    patente = models.ForeignKey(Booking, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_service'
