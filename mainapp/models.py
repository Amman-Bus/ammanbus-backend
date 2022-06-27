from pyexpat import model
from turtle import distance
from django.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=50)
    lon = models.FloatField()
    lat= models.FloatField()
    used_route= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Route(models.Model):
    name=models.CharField(max_length=50)
    start_time=models.TimeField(auto_now=False, auto_now_add=False)
    end_time=models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name

class StationStop(models.Model):
    route=models.ForeignKey(Route,related_name='station_stops',on_delete=models.CASCADE)
    station=models.ForeignKey(Station,on_delete=models.CASCADE)
    order_number=models.IntegerField()
    time_to_next_station=models.IntegerField()
    distance_to_next_station=models.IntegerField()
    class Meta:
        unique_together = ['route', 'station']
        ordering = ['order_number']


class Bus(models.Model):
    bus_name=models.CharField(max_length=50)
    route_id=models.IntegerField()
    capacity=models.IntegerField()
    driver_id=models.CharField(max_length=50)


class BusStationStop(models.Model):
    bus_id=models.IntegerField()
    route_id=models.IntegerField()
    time=models.TimeField(auto_now=False, auto_now_add=False)

