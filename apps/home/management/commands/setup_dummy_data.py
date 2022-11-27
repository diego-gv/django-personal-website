
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "This command generate a dummy data for simulate complete use"

    def handle(self, *args, **kwargs):
        self.stdout.write("Preparing users dummy data...")
        call_command("setup_dummy_users")
        self.stdout.write("Preparing project dummy data...")
        call_command("setup_dummy_projects")
        self.stdout.write("Preparing posts dummy data...")
        call_command("setup_dummy_posts")
