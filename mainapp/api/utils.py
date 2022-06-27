from rest_framework.response import Response

from mainapp.models import Station,Route,Bus,StationStop
from .serializers import StationSerializer,RouteSerializer,BusSerializer,StationStopSerializer
#for function based views
"""
def getStationsList(request):
    stations = Station.objects.all().order_by('-id')
    serializer = StationSerializer(stations, many=True)
    return Response(serializer.data)


def getStationsDetail(request, pk):
    station = Station.objects.get(id=pk)
    serializer = StationSerializer(station, many=False)
    return Response(serializer.data)


def createStation(request):
    data = request.data
    station = Station.objects.create(
        name=data['name'],
        lon=data['lon'],
        lat=data['lat'],
        used_route=data['used_route']
    )
    serializer = StationSerializer(station, many=False)
    return Response(serializer.data)

def updateStation(request, pk):
    data = request.data
    station = Station.objects.get(id=pk)
    serializer = StationSerializer(instance=station, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def deleteStation(request, pk):
    station = Station.objects.get(id=pk)
    station.delete()
    return Response({'sucess': True})"""


