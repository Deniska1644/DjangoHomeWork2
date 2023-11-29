from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            user = User(name=f'Name{i}', email=f'john@example{i}.com',
                        phone_number=f'+7{i*111111111}', address=f'Marks{i}')
            user.save()
            self.stdout.write(f'{user}')
