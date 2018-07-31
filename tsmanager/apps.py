from django.apps import AppConfig


class TechnostallManagerConfig(AppConfig):
    name = 'tsmanager'

    def ready(self):
        import tsmanager.signals
