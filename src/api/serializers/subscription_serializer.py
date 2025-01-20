from rest_framework import serializers
from subscription.models import SubscriptionModel
from api.serializers.prospect_serializer import PersonSerializer
from api.serializers.vehicle_serializer import VehicleSerializer
from user.models.prospect_model import ProspectModel
from vehicle.models.vehicle_model import VehicleModel


class SubscriptionSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    vehicle = VehicleSerializer()
    class Meta:
        model = SubscriptionModel
        fields = [
            'id',
            'person',
            'vehicle',
            'produit',
            'date_souscription',
            'statut',
            'numero_attestation',
            'user'
        ]
        read_only_fields = ['id', 'date_souscription','user', 'numero_attestation']
    
    def create(self, validated_data):
        print(validated_data)
        person_data = validated_data.pop('person')
        vehicle_data = validated_data.pop('vehicle')

        # Create related person and vehicle objects
        person_instance = ProspectModel.objects.create(**person_data)
        vehicle_instance = VehicleModel.objects.create(**vehicle_data)

        # Create the subscription instance with the related person and vehicle
        subscription = SubscriptionModel.objects.create(
            person=person_instance,
            vehicle=vehicle_instance,
            **validated_data
        )
        return subscription