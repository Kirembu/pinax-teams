from django.conf.urls import include, url

urlpatterns = [
    url(r"^account/", include("zerxis_account.urls")),
    url(r"^", include("zerxis_teams.teams.urls", namespace="zerxis_teams")),
]
