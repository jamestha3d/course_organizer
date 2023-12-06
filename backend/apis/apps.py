from django.apps import AppConfig


class ApisConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apis"

    def ready(self):
        import apis.signals #overwriting ready method so that signals.py imports will work