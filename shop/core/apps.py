from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'core'

    def ready(self)->None:
        """
        Needs for connecting signals\n
        @return None
        """
        import core.signals