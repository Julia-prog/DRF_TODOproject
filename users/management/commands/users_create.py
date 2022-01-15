from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Create users and superuser to test'

    def handle(self, *args, **options):
        User.objects.all().delete()

        for i in range(5):
            user = User.objects.create_user(first_name=f'Иван{i + 1}',
                                       last_name=f'Петров{i + 1}',
                                       username=f'Ivan{i + 1}',
                                       email=f'{i + 1}@gmail.com')
            print(f'user {user} created')

        User.objects.create_superuser(first_name='Админ', last_name='Петров', username='admin',
                                      password='Aa12345@', email='email@yandex.ru')

        print('done')
