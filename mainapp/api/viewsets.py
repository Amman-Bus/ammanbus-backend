from datetime import datetime, timedelta
from math import ceil

import networkx as nx
from django.http import JsonResponse
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from mainapp.models import Station, Route, StationStop, FareTable, Bus, Driver
from .serializers import StationSerializer, RouteSerializer, StationStopSerializer, BusSerializer, DriverSerializer


class IsDriver(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_driver:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.driver.user == request.user:
            return True
        return False


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class StationStopViewSet(viewsets.ModelViewSet):
    queryset = StationStop.objects.all()
    serializer_class = StationStopSerializer

    def get_permissions(self):

        # Instantiates and returns the list of permissions that this view requires.
        # actions : list, create , retrive , update, partial_update,destroy
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser | IsDriver]
        return [permission() for permission in permission_classes]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


@api_view(['GET'])
@permission_classes([AllowAny])
def get_buses_for_route(request, route_id):
    buses_list = Bus.objects.filter(route_id=route_id)
    return Response(BusSerializer(buses_list, many=True).data)


@api_view(['GET'])
@permission_classes([AllowAny])
def find_route(request, from_id, to_id):
    from_station = Station.objects.get(id=from_id)
    to_station = Station.objects.get(id=to_id)
    if to_station == from_station:
        return Response({'error': "same stations"})
    graph = build_graph()
    paths = list(nx.shortest_simple_paths(graph, from_station.id, to_station.id, weight='time'))
    return Response({'paths': build_directions_response(graph, paths)})


def build_graph():
    graph = nx.Graph()
    routes = Route.objects.all()
    overlap_stations = {}
    for route in routes:
        station_stops = route.station_stops.all()
        for i in range(len(station_stops) - 1):
            graph.add_edges_from([(station_stops[i].id, station_stops[i + 1].id,
                                   {"time": station_stops[i].time_to_next_station,
                                    "distance": station_stops[i].distance_to_next_station, })])
            add_overlap_stations_edge(graph, station_stops[i], overlap_stations)
            if i == len(station_stops) - 2:
                add_overlap_stations_edge(graph, station_stops[i + 1], overlap_stations)

    # print(graph.edges.data())
    return graph


def add_overlap_stations_edge(graph, station_stop, overlap_stations):
    if station_stop.station_id in overlap_stations:
        for stop_id in overlap_stations[station_stop.station_id]:
            graph.add_edges_from([(station_stop.id, stop_id,
                                   {"time": 1, "distance": 0})])

        overlap_stations[station_stop.station_id].append(station_stop.id)
    else:
        overlap_stations[station_stop.station_id] = [station_stop.id]


def build_directions_response(graph, paths):
    paths_json = []
    for path in paths:

        total_time = nx.path_weight(graph, path, weight='time')  # Calculate total time
        total_distance = nx.path_weight(graph, path, weight='distance')  # Calculate distance time
        fare = calculate_fare(total_distance)
        station_stops = get_station_stops_for_path(path)
        current_route = station_stops[0].route
        now = datetime.now() + timedelta(minutes=2)
        current_route_dic = {"route_name": current_route.name,
                             "start_time": now.strftime("%m/%d/%Y, %H:%M:%S"), "station_stops": []}
        routes = [current_route_dic]
        accumulate_time = 0
        for stop in station_stops:
            pre_stop = stop
            if pre_stop:
                accumulate_time += pre_stop.time_to_next_station
            if current_route != stop.route:
                start_time = now + timedelta(minutes=accumulate_time)
                current_route = stop.route
                current_route_dic = {"route_name": current_route.name,
                                     "start_time": start_time.strftime("%m/%d/%Y, %H:%M:%S"), "station_stops": []}
                routes.append(current_route_dic)

            current_route_dic["station_stops"].append(StationStopSerializer(stop).data)
        paths_json.append({"path": 1, "total_time": total_time,
                           "distance": total_distance, "fare": fare, "routes": routes})
    return paths_json


def get_station_stops_for_path(path):
    station_stops = []
    path_graph = nx.path_graph(path)
    edge0 = list(path_graph.edges(data=True))[0]
    station_stops.append(StationStop.objects.get(id=edge0[0]))
    for ea in path_graph.edges():
        station_stops.append(StationStop.objects.get(id=ea[1]))
    return station_stops


def calculate_fare(distance):
    return FareTable.objects.get(id=1).fare + (FareTable.objects.get(id=2).fare * ceil(distance / 1000))
