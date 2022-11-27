import random

from django.core.management import BaseCommand
from django.db import transaction

from apps.users.factories import AdminUserFactory, UserFactory
from apps.users.models import User


class Command(BaseCommand):
    help = "This command generate a dummy data for simulate complete use"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [User]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        AdminUserFactory()
        UserFactory(username='garvi', password='garvi', email='garvi@example.com')
