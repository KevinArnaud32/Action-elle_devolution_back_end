import random
import string
from subscription.models import SubscriptionModel
from api.serializers.subscription_serializer import SubscriptionSerializer      
from rest_framework import viewsets
from django.db import transaction
from rest_framework.validators import ValidationError
from vehicle.models.category_model import CategoryModel
from rest_framework.decorators import action
from rest_framework.response import Response


class SubscriptionViewset(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer  
    queryset = SubscriptionModel.objects.all()
    http_method_names = ['get', 'post']

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        category = self.request.data.get('vehicle').get('category')
        category = CategoryModel.objects.get(id=category)
        produit = self.request.data.get('produit')
        if produit == 'Papillon':
            if int(category.code) != 201:
                raise ValidationError({"detail": "Produit Papillon disponible uniquement pour la catégorie Promenade et Affaire"})
        elif produit == 'Douby':
            if int(category.code) != 202:
                raise ValidationError({"detail": "Produit Douby disponible uniquement pour la catégorie Véhicules Motorisés à 2 ou 3 roues"})
        elif produit == 'Douyou':
            if int(category.code) != 201 or int(category.code) != 202:
                raise ValidationError({"detail": "Produit Douyou disponible uniquement pour la catégorie Promenade et Affaire et Véhicules Motorisés à 2 ou 3 roues"})
        elif produit == 'Toutourisquou':
            if int(category.code) != 201:
                raise ValidationError({"detail": "Produit Toutourisquou disponible uniquement pour la catégorie Promenade et Affaire"})
        serializer.save(user=user)


    
    @action(detail=True, methods=['get'])
    def attestation(self, request, pk=None):
        subscription = self.get_object()
        subscription_data = self.get_serializer(subscription).data
        return Response(subscription_data)
    
