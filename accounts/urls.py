from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),
    path('passenger_register/', views.passenger_register.as_view(), name='passenger_register'),
    path('driver_register/', views.driver_register.as_view(), name='driver_register')
]