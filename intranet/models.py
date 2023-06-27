from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    rut = models.CharField(max_length=9, default=12345678)
    birthday = models.DateField(null=True)
    GENDER_CHOICES = (('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Otro'))
    gender = models.CharField(max_length=1, default='H', choices=GENDER_CHOICES)


class Service(models.Model):
    id = models.AutoField(db_column='serviceID', primary_key=True)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'service'


class Booking(models.Model):
    id = models.AutoField(db_column='bookingID', primary_key=True)
    patente = models.CharField(max_length=8)
    service = models.ForeignKey(Service, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commentary = models.CharField(blank=True, max_length=128)

    class Meta:
        db_table = 'booking'
