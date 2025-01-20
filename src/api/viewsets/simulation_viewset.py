from datetime import timedelta
from django.utils import timezone
from simulation.models import SimulationModel
from api.serializers.simulation_serializer import SimulationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import random
import string
from rest_framework import permissions
from user.models.user_model import UserModel
from vehicle.models.category_model import CategoryModel
from rest_framework.exceptions import ValidationError


class SimulationViewset(viewsets.ModelViewSet):
    serializer_class = SimulationSerializer
    queryset = SimulationModel.objects.all()
    http_method_names = ['get', 'post']
    
    def perform_create(self, serializer):
        user = self.request.user
        # Récupérer les données fournies par l'utilisateur
        puissance_fiscale = int(self.request.data.get('puissance_fiscale'))
        valeur_venale = float(self.request.data.get('valeur_venale'))
        valeur_neuve = float(self.request.data.get('valeur_neuve'))
        produit = self.request.data.get('type_produitAssurance')
        annee = self.request.data.get('annee_vehicule')
        category = self.request.data.get('category')
        category = CategoryModel.objects.get(id=category)
        # Calcul de la prime RC selon la puissance fiscale
        prime_rc = self.calculate_rc(puissance_fiscale)

        # Calcul des primes en fonction des garanties incluses dans le produit
        prime_domages = 0
        prime_tierce_collision = 0
        prime_tierce_plafonnee = 0
        prime_vol = 0
        prime_incendie = 0
        if produit == 'Papillon':
            if int(category.code) != 201:
                raise ValidationError({"detail": "Produit Papillon disponible uniquement pour la catégorie Promenade et Affaire"})
            prime_domages = 0.026 * valeur_neuve if 0 <= annee <= 5 else 0
            prime_vol = 0.0014 * valeur_venale 
        elif produit == 'Douby':
            if int(category.code) != 202:
                raise ValidationError({"detail": "Produit Douby disponible uniquement pour la catégorie Véhicules Motorisés à 2 ou 3 roues"})
            prime_domages = 0.026 * valeur_venale if 0 <= annee <= 5 else 0
            prime_tierce_collision = 0.0165 * valeur_neuve if 0 <= annee <= 8 else 0
        elif produit == 'Douyou':
            if int(category.code) != 201 or int(category.code) != 202:
                raise ValidationError({"detail": "Produit Douyou disponible uniquement pour la catégorie Promenade et Affaire et Véhicules Motorisés à 2 ou 3 roues"})
            prime_domages = 0.026 * valeur_neuve if 0 <= annee <= 5 else 0
            prime_vol = 0.0014 * valeur_venale
            prime_incendie = 0.0015 * valeur_venale
        elif produit == 'Toutourisquou':
            print(category.code)
            if int(category.code) != 201:
                raise ValidationError({"detail": "Produit Toutourisquou disponible uniquement pour la catégorie Promenade et Affaire"})
            prime_domages = 0.026 * valeur_neuve if 0 <= annee <= 5 else 0
            prime_tierce_collision = 0.0165 * valeur_neuve if 0 <= annee <= 8 else 0
            prime_vol = 0.0014 * valeur_venale
            prime_incendie = 0.0015 * valeur_venale
            prime_tierce_plafonnee = 0.042 * valeur_venale if 0 <= annee <= 10 else 0
        
        # Calcul du total
        total = prime_rc + prime_domages + prime_tierce_collision + prime_vol + prime_incendie + prime_tierce_plafonnee

        # Générer la référence de devis
        quote_reference = 'QT' + ''.join(random.choices(string.ascii_letters + string.digits, k=12))

        # Enregistrer la simulation avec les données calculées
        simulation = serializer.save(
            user=user,
            price=total,
            quoteReference=quote_reference,
            date_creation=timezone.now(),
            endDate=timezone.now() + timedelta(weeks=2)
        )

        return simulation

    def calculate_rc(self, puissance_fiscale):
        """Calcule la prime RC selon la puissance fiscale."""
        if puissance_fiscale <= 2:
            return 37601
        elif 3 <= puissance_fiscale <= 6:
            return 45181
        elif 7 <= puissance_fiscale <= 10:
            return 51078
        elif 11 <= puissance_fiscale <= 14:
            return 65677
        elif 15 <= puissance_fiscale <= 23:
            return 86456
        else:
            return 104143

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        return Response({
            "success": True,
            "data": {
                "message": "Simulation créée avec succès",
                "details": response.data,
                "code": response.status_code
            }
        }, status=status.HTTP_201_CREATED)
