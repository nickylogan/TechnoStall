from django.apps import AppConfig


class TechnostallManagerConfig(AppConfig):
    name = 'technostall_manager'

    def ready(self):
        import technostall_manager.signals
