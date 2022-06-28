from rest_framework.serializers import ModelSerializer
from driversapp.models import DriverApp


class DriverAppSerializer(ModelSerializer):
    class Meta:
        model = DriverApp
        fields = '__all__'