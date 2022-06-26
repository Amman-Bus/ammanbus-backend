from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import Passenger, Driver, User

class PassengerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zip_code = forms.CharField(required=True)
    credit_card_number = forms.CharField(required=True)
    credit_card_expiration_date = forms.CharField(required=True)
    credit_card_security_code = forms.CharField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_passenger = True
        user.save()
        passenger = Passenger.objects.create(user=user)
        passenger.phone_number = self.cleaned_data.get('phone_number')
        passenger.area_name = self.cleaned_data.get('area_name')
        passenger.save()
        return user


class DriverSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    department = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    driver_address = forms.CharField(required=True)
    driver_email = forms.CharField(required=True)
    driver_city = forms.CharField(required=True)
    driver_state = forms.CharField(required=True)
    driver_zip_code = forms.CharField(required=True)
    driver_national_id = forms.CharField(required=True)
    driver_credit_card_number = forms.CharField(required=True)
    driver_credit_card_expiration_date = forms.CharField(required=True)
    driver_credit_card_security_code = forms.CharField(required=True)
    driver_iban_code = forms.CharField(required=True)
    
    # driver personal license information
    driver_license_number = forms.CharField(required=True)
    driver_license_expiration_date = forms.CharField(required=True)
    
    # driver bus information
    bus_make = forms.CharField(required=True)
    bus_model = forms.CharField(required=True)
    bus_license_number = forms.CharField(required=True)
    bus_license_expiration_date = forms.CharField(required=True)
    bus_license_security_code = forms.CharField(required=True)
    bus_license_plate_number = forms.CharField(required=True) 
    bus_license_plate_expiration_date = forms.CharField(required=True)
    bus_license_plate_security_code = forms.CharField(required=True)
    bus_license_plate_city = forms.CharField(required=True)
    bus_license_plate_zip_code = forms.CharField(required=True)



    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_driver = True
        user.save()
        driver = driver.objects.create(user=user)
        driver.phone_number = self.cleaned_data.get('phone_number')
        driver.department = self.cleaned_data.get('department')
        driver.save()
        return user