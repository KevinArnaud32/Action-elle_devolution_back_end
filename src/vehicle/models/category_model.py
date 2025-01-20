from django.db import models

class CategoryModel(models.Model):
    code = models.CharField(max_length=10)
    libelle = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.code

 