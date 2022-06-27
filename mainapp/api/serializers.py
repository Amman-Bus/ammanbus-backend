from rest_framework.serializers import ModelSerializer
from mainapp.models import Station,Route,Bus,StationStop


class StationSerializer(ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class StationStopSerializer(ModelSerializer):
    
    class Meta:
        model = StationStop
        fields = '__all__'

class RouteSerializer(ModelSerializer):
    station_stops = StationStopSerializer(many=True, read_only=True)
    class Meta:
        model = Route
        fields = '__all__'


class BusSerializer(ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'



