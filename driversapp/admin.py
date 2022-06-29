from django.contrib import admin
from .models import DriverApp

# Register your models here.

@admin.register(DriverApp)
class DriverAppAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone_number', 'email', 'driver_license', 'location_gps')