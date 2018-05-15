from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
    # layout = 'vertical'

class MyAppConfig(AppConfig):
    name = 'MyApp'
