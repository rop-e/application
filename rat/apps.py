from django.apps import AppConfig


class RatConfig(AppConfig):
    name = 'rat'
    verbose_name = 'Registro de Acidente de Transito'
    verbose_name_plural = 'Registros de Acidente de Transito'
    
    def ready(self):
        import rat.signals
