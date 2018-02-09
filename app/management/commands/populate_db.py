from django.core.management.base import BaseCommand
from app.models import Team, Player


class Command(BaseCommand):
    args = '<foo bar ...'
    help = 'help_string'

    def _populate_db(self):
        count = 200

        all_users = Player.objects.all()
        for user in all_users:
            print(user)
        print(len(all_users))

        new_user = Player(username="name123", surname="surname12")
        new_user.save()

    def handle(self, *args, **options):
        self._populate_db()

