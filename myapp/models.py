from django.db import models

# Create your models here.
class Person(models.Model):

     # Map person details which we want to store in db

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)