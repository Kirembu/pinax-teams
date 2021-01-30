import pkg_resources

__version__ = pkg_resources.get_distribution("zerxis_teams").version

default_app_config = "zerxis_teams.teams.apps.AppConfig"
