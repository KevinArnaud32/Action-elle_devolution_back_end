from django.db import models


class ProspectModel(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    ville = models.CharField(max_length=100)
  

    def __str__(self):
        return f"{self.prenom} {self.nom}"