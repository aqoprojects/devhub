from django.apps import AppConfig


class DevsocialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'devsocial'


    def ready(self):
        import devsocial.signal