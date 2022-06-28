from django.urls import path, include
from rest_framework.routers import DefaultRouter
from driversapp import views

router = DefaultRouter()
router.register(r'driverapp', views.DriverAppView, basename='driverapp')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]