#!/usr/bin/env python
import os
import sys

import django


def run(*args):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zerxis_teams.teams.tests.settings")
    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    django.core.management.call_command(
        "makemigrations",
        "zerxis_teams",
        *args
    )


if __name__ == "__main__":
    run(*sys.argv[1:])
