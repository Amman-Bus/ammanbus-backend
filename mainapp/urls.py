from django.urls import path, include
from rest_framework import routers

from mainapp.api.viewsets import StationViewSet, RouteViewSet, StationStopViewSet, find_route, get_buses_for_route, \
    BusViewSet, DriverViewSet
from rest_framework_simplejwt import views as jwt_views
# from mainapp.api.viewsets import getStations, getStation,createStationaApi,deleteStationApi,updateStationApi

router = routers.DefaultRouter()
router.register(r'stations', StationViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'station-stop', StationStopViewSet)
router.register(r'buses', BusViewSet)
router.register(r'drivers', DriverViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('find/<str:from_id>/<str:to_id>', find_route, name='find-route'),
    path('busesForRoute/<str:route_id>', get_buses_for_route, name='get_buses_for_route'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

   
]




# for the function based views

"""path('list/', getStations , name="stations"),
    path('detail/<str:pk>',getStation, name='detail-station'),
    path('create/',createStationaApi, name='create-station'),
    path('detail/<str:pk>/update',updateStationApi, name='update-station'),
    path('detail/<str:pk>/delete',deleteStationApi, name='detail-station')"""