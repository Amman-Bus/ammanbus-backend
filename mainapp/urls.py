from django.urls import path , include
#from mainapp.api.viewsets import getStations, getStation,createStationaApi,deleteStationApi,updateStationApi



from rest_framework import routers, serializers, viewsets
from mainapp.api.viewsets import StationViewSet,RouteViewSet,StationStopViewSet,find_route

router = routers.DefaultRouter()
router.register(r'stations', StationViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'stationstop', StationStopViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('find/<str:from_id>/<str:to_id>', find_route, name='find-route'),

   
]




# for the function based views

"""path('list/', getStations , name="stations"),
    path('detail/<str:pk>',getStation, name='detail-station'),
    path('create/',createStationaApi, name='create-station'),
    path('detail/<str:pk>/update',updateStationApi, name='update-station'),
    path('detail/<str:pk>/delete',deleteStationApi, name='detail-station')"""