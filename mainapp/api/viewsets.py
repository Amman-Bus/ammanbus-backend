from rest_framework.decorators import api_view,permission_classes
from rest_framework.serializers import Serializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
#from .utils import getStationsList,getStationsDetail,createStation,updateStation,deleteStation

from mainapp.models import Station,Route,StationStop
from rest_framework import routers, serializers, viewsets
from .serializers import StationSerializer,RouteSerializer,StationStopSerializer

from rest_framework.response import Response

import networkx as nx

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



@api_view(['GET'])
@permission_classes([AllowAny])
def find_route(request, from_id, to_id):
    from_station = Station.objects.get(id=from_id)
    to_station = Station.objects.get(id=to_id)
    graph = build_graph()
    paths = list(nx.shortest_simple_paths(graph, from_station.id, to_station.id, weight='weight'))
    #print(nx.path_weight(graph, paths[0], weight='weight')) #Calculate total time
    station_list = []
    path_graph = nx.path_graph(paths[0])
    edge0 = list(path_graph.edges(data=True))[0]
    station_list.append(Station.objects.get(id=edge0[0]))
    for ea in path_graph.edges():
        # print from_node, to_node, edge's attributes
        #print(ea[1])
        station_list.append(Station.objects.get(id=ea[1]))
    serializer = StationSerializer(station_list, many=True)
    return Response(serializer.data)


def build_graph():
    G = nx.Graph()
    routes = Route.objects.all()
    for route in routes:
        station_list = route.station_stops.all()
        for i in range(len(station_list)-1):
            G.add_edges_from([(station_list[i].station.id,station_list[i+1].station.id,
                               {"weight": station_list[i].time_to_next_station, "route": route.name})])
    #print(G.edges.data())
    return G