from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator


# Create your models here.

class DriverApp(models.Model):

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100, default=1)
    password = models.CharField(max_length=100)
    driver_license = models.IntegerField(default=1)
    driver_id_number = models.IntegerField(default=1)
    bus_id = models.IntegerField(default=1)
    start_route_at = models.CharField(max_length=100, default="")
    end_route_at = models.CharField(max_length=100, default="")
    location_gps = models.CharField(max_length=100, default="")
    iban_number = models.CharField(max_length=100, validators=[alphanumeric])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    capacity = models.IntegerField(default=1)
    

    def __str__(self):
        return self.user_name