#region             -----External Imports-----
from django.apps import AppConfig
#endregion

class CoreConfig(AppConfig):
    name = 'core'

    def ready(self)->None:
        """
        Connects app's signals\n
        @return None
        """
        import core.signals