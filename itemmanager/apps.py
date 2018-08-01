from django.apps import AppConfig


class ItemManagerConfig(AppConfig):
    name = 'itemmanager'

    def ready(self):
        import itemmanager.signals