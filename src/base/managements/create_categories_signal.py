from django.db.models.signals import post_migrate
from django.dispatch import receiver
from vehicle.models.category_model import CategoryModel

@receiver(post_migrate)
def create_categories(sender, **kwargs):
    # Vérifiez si c'est le bon modèle pour éviter les doublons
    if sender.name == 'base':  # Remplacez 'your_app_name' par le nom de votre application
        categories_data = [
            {'code': '201', 'libelle': 'Promenade et Affaire', 'description': 'Usage personnel'},
            {'code': '202', 'libelle': 'Véhicules Motorisés à 2 ou 3 roues', 'description': 'Motocycle, tricycles'},
            {'code': '203', 'libelle': 'Transport public de voyage', 'description': 'Véhicule transport de personnes'},
            {'code': '204', 'libelle': 'Véhicule de transport avec taximètres', 'description': 'Taxis'},
        ]

        for category in categories_data:
            CategoryModel.objects.get_or_create(
                code=category['code'],
                defaults={
                    'libelle': category['libelle'],
                    'description': category['description'],
                }
            )