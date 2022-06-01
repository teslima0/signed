from django.apps import AppConfig


class DjangoFbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_fb'

    def ready(self):
        import django_fb.signals


