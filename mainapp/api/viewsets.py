from rest_framework.decorators import api_view,permission_classes
from rest_framework.serializers import Serializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
#from .utils import getStationsList,getStationsDetail,createStation,updateStation,deleteStation

from mainapp.models import Station,Route,StationStop
from rest_framework import routers, serializers, viewsets
from .serializers import StationSerializer,RouteSerializer,StationStopSerializer

# Create your views here.
# function based views
"""@api_view(['GET'])
@permission_classes([AllowAny])
def getStations(request):
    return getStationsList(request)

@api_view(['GET'])
@permission_classes([AllowAny])
def getStation(request, pk):
    return getStationsDetail(request, pk)

   

@api_view(['POST'])
@permission_classes([AllowAny])
def createStationaApi(request):
    return createStation(request)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def deleteStationApi(request, pk):
    return deleteStation(request, pk)


@api_view(['PUT'])
@permission_classes([AllowAny])
def updateStationApi(request, pk):
    return updateStation(request, pk)"""



class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    def get_permissions(self):
    
    
    
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get_permissions(self):
    
    
    
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class StationStopViewSet(viewsets.ModelViewSet):
    queryset = StationStop.objects.all()
    serializer_class = StationStopSerializer

    def get_permissions(self):
    
    #Instantiates and returns the list of permissions that this view requires.
    # actions : list, create , retrive , update, partial_update,destroy
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]