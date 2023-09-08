import os
from django.core.management.base import BaseCommand

from authentication.models import User


SUPERUSER_NAME = os.environ.get("DJANGO_ADMIN_LOGIN")
SUPERUSER_PASSWORD = os.environ.get("DJANGO_ADMIN_PASSWORD")
SUPERUSER_EMAIL = os.environ.get("DJANGO_ADMIN_EMAIL")


class Command(BaseCommand):
    help = "Script dédié à intégrer différents éléments pour des tests."

    def handle(self, *args, **kwargs):
        """
        Description:
        Création compte administrateur de l'application.
        """
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(SUPERUSER_NAME, SUPERUSER_EMAIL, SUPERUSER_PASSWORD)
