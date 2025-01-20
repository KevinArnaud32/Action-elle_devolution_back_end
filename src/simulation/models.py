from datetime import timedelta
from django.db import models
from django.utils import timezone
from user.models.user_model import UserModel
from user.models.prospect_model import ProspectModel
from vehicle.models.category_model import CategoryModel
from django.utils.crypto import get_random_string


class SimulationModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_simulation')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='category_simulation')
    quoteReference = models.CharField(max_length=20, unique=True, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(null=True, blank=True)
    type_produitAssurance = models.CharField(max_length=20, null=True, blank=True)
    valeur_venale = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    valeur_neuve = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    puissance_fiscale = models.PositiveIntegerField(null=True, blank=True)
    annee_vehicule = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.quoteReference
