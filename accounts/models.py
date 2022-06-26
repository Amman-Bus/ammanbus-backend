from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_passenger = models.BooleanField(default=False)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

class Passenger(models.Model):
    # passenger personal information
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
  
class Driver(models.Model):
    # driver personal information
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    department = models.CharField(max_length=30)


    