from pyexpat import model
from turtle import distance
from django.db import models

# Create your models here.
from accounts.models import User


class Station(models.Model):
    name = models.CharField(max_length=50)
    lon = models.FloatField()
    lat = models.FloatField()
    used_route = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class StationStop(models.Model):
    route = models.ForeignKey(Route, related_name='station_stops', on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    time_to_next_station = models.IntegerField()
    distance_to_next_station = models.IntegerField()

    def __str__(self):
        return f'{self.route}-{self.station}-{self.order_number}'

    class Meta:
        unique_together = ['route', 'station']
        ordering = ['route']


class Driver(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    birth = models.DateField()


1


class Bus(models.Model):
    bus_name = models.CharField(max_length=50)
    route = models.ForeignKey(Route, related_name='buses', on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField()
    current_capacity = models.IntegerField()
    driver = models.OneToOneField(Driver, related_name='driver', on_delete=models.SET_NULL, null=True, blank=True)
    lon = models.FloatField()
    lat = models.FloatField()
    reverse = models.BooleanField()


class BusStationStop(models.Model):
    bus_id = models.IntegerField()
    route_id = models.IntegerField()
    time = models.TimeField(auto_now=False, auto_now_add=False)


class FareType(models.IntegerChoices):
    base = 0, 'Base'
    distance = 1, 'Distance'


class FareTable(models.Model):
    fare = models.FloatField()
    fare_type = models.IntegerField(default=FareType.base, choices=FareType.choices)
