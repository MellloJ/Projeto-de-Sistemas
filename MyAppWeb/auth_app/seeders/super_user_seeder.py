from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from django.contrib.auth import get_user_model

class SuperUserSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'SuperUserSeeder'

    def seed(self):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                nomeCompleto='Admin User',
                email='admin@example.com',
                password='123456789',
                first_name='Admin',
                last_name='User'
            )
            self.succes(f'Super User created')
        else:
            self.error(f'Super User already exists')