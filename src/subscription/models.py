from django.db import models
from user.models.user_model import UserModel
from vehicle.models.vehicle_model import VehicleModel 
from user.models.prospect_model import ProspectModel
import random
import string


class SubscriptionModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_subscription')
    person = models.ForeignKey(ProspectModel, on_delete=models.CASCADE, related_name='person_subscription')
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, related_name='vehicle_subscription')
    produit = models.CharField(max_length=20)
    date_souscription = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, default='en attente')
    numero_attestation = models.CharField(max_length=50, null=True, blank=True, unique=True)

    def __str__(self):
        return f"Souscription {self.id} - {self.statut}"

    def save(self, *args, **kwargs):
        if not self.numero_attestation:
            self.numero_attestation = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        super().save(*args, **kwargs)