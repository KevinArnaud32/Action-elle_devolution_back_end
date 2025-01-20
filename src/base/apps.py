from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        from base.managements.create_admin_signal import create_admin
        from base.managements.create_categories_signal import create_categories