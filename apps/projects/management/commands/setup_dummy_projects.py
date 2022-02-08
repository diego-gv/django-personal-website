import random

from django.core.management import BaseCommand
from django.db import transaction

from apps.projects.factories import ProjectFactory
from apps.projects.models import Project


class Command(BaseCommand):
    help = "This command generate a dummy data for simulate complete use"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Project]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        for i in range(4):
            ProjectFactory(image=random.choice(['img/django_logo.png', 'img/flask_logo.png']))
