from django.shortcuts import render
from rest_framework import viewsets
from .api.serializers import DriverAppSerializer
from .models import DriverApp

# Create your views here.

class DriverAppView(viewsets.ModelViewSet):
    serializer_class = DriverAppSerializer
    queryset = DriverApp.objects.all()

