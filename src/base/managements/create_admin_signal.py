from django.db.models.signals import post_migrate
from django.dispatch import receiver
from user.models.user_model import UserModel

@receiver(post_migrate)
def create_admin(sender, **kwargs):
    if sender.name == 'base':
        user_data = [
            {'username': 'admin', 'role': 'admin', 'password': 'admin', 'email': 'admin@yopmail', 'first_name': 'admin', 'last_name': 'admin'},
        ]

        for user in user_data:
            UserModel.objects.get_or_create(**user)

