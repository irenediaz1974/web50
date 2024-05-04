from django.apps import AppConfig


class AuctionsConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField' # Para que no cree BigAutoField por default
    name = 'auctions'
