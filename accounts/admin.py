from lib2to3.pgen2.driver import Driver
from django.contrib import admin
from .models import Passenger, Driver
# Register your models here.

admin.site.register(Driver)
admin.site.register(Passenger)