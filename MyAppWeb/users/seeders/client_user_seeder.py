from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from django.contrib.auth import get_user_model
from django.utils.timezone import now

class ClientUserSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'ClientUserSeeder'

    def seed(self):
        from users.models import ClientUser  # Ajuste o import conforme o local do seu modelo
        User = get_user_model()
        if not User.objects.filter(email='clientuser@example.com').exists():
            user = User.objects.create_user(
                email='clientuser@example.com',
                password='123456789',
                user_type='client',
                is_active=True
            )
            ClientUser.objects.create(
                user=user,
                cpf='67748520097',
                first_name='Cliente',
                last_name='Teste',
            )
            self.succes('Client User and ClientUser created')
        else:
            self.error('Client User already exists')