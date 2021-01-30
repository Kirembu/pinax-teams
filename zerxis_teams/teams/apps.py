from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _

try:
    import importlib
except ImportError:
    from django.utils import importlib


class AppConfig(BaseAppConfig):

    name = "zerxis_teams.teams"
    label = "zerxis_teams"
    verbose_name = _("Zerxis Teams")

    def ready(self):
        importlib.import_module("zerxis_teams.teams.receivers")
