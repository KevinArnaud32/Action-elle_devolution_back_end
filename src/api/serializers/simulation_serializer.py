from rest_framework import serializers
from simulation.models import SimulationModel

class SimulationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimulationModel
        fields = [
            "id" , "category", "puissance_fiscale", "valeur_venale", "type_produitAssurance","quoteReference", "price", "date_creation", "endDate",
            "valeur_neuve", "annee_vehicule", "user"
        ]
        read_only_fields = ["id", "quoteReference", "price", "date_creation", "endDate", 'user']