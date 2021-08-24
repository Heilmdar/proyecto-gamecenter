from django.apps import AppConfig


class VentasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ventas'
    verbose_name='Registro de ventas'


class NosotrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nosotros'
    verbose_name='Informacion de desarrolladores'
