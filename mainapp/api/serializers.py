from rest_framework.serializers import ModelSerializer
from mainapp.models import Station, Route, Bus, StationStop, Driver


class StationSerializer(ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class StationStopSerializer(ModelSerializer):
    station = StationSerializer(required=False)

    class Meta:
        model = StationStop
        fields = '__all__'


class RouteSerializer(ModelSerializer):
    station_stops = StationStopSerializer(many=True, read_only=True)

    class Meta:
        model = Route
        fields = '__all__'

class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class BusSerializer(ModelSerializer):
    driver = DriverSerializer(required=False)
    class Meta:
        model = Bus
        fields = '__all__'


