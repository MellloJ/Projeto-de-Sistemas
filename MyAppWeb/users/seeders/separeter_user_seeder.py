from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from django.contrib.auth import get_user_model
from django.utils.timezone import now

class SeparaterUserSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'SeparaterUserSeeder'

    def seed(self):
        from users.models import SeparaterUser
        User = get_user_model()
        if not User.objects.filter(email='separater@example.com').exists():
            user = User.objects.create_user(
                email='separater@example.com',
                password='123456789',
                is_active=True,
                user_type='separater',
            )
            SeparaterUser.objects.create(
                user=user,
                first_name='Separador',
                last_name='Teste',
                cpf='36396715031'
            )
            self.succes('Separater User and SeparaterUser created')
        else:
            self.error('Separater User already exists')