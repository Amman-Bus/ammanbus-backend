from django.contrib import admin

from .models import Station, Route, Bus, StationStop, BusStationStop, FareTable, Driver

# Register your models here.
admin.site.register(Station)
admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(StationStop)
admin.site.register(BusStationStop)
admin.site.register(FareTable)
admin.site.register(Driver)