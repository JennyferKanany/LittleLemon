from django.db import models

# Create your models here.
class Menu(models.Model):
    title =  models.CharField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inventory = models.IntegerField(default=0)


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()
