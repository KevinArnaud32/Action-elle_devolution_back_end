from rest_framework import serializers
from vehicle.models.vehicle_model import VehicleModel

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleModel
        fields = "__all__"