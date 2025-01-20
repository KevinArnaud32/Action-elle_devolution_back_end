from django.db import models
from user.models.prospect_model import ProspectModel
from vehicle.models.category_model import CategoryModel

class VehicleModel(models.Model):
    # person = models.ForeignKey(PersonModel, on_delete=models.CASCADE, related_name='person_vehicle')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='category_vehicle')
    immatriculation = models.CharField(max_length=20, unique=True)
    couleur = models.CharField(max_length=30)
    puissance_fiscale = models.PositiveIntegerField()
    date_premiere_mise_en_circulation = models.DateField()
  
    def __str__(self):
        return self.immatriculation
