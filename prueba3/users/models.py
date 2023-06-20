from django.db import models


class Gender(models.Model):
    id = models.AutoField(db_column='genderId', primary_key=True)
    gender = models.CharField(max_length=20, blank=False, null=False)


class User(models.Model):
    id = models.AutoField(db_column='userId', primary_key=True)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthdate = models.DateField(blank=False, null=False)
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE, db_column='genderId')
    active = models.IntegerField()
