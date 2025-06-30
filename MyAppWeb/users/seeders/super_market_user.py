from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from django.contrib.auth import get_user_model
from django.utils.timezone import now

class SupermarketUserSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'SupermarketUserSeeder'

    def seed(self):
        from users.models import SupermarketUser  # Ajuste o import conforme o local do seu modelo
        User = get_user_model()
        if not User.objects.filter(email='market@example.com').exists():
            user = User.objects.create_user(
                email='market@example.com',
                password='123456789',
                is_active=True,
                user_type='supermarket'
            )
            SupermarketUser.objects.create(
                user=user,
                fantasy_name='Supermercado Exemplo',
                cnpj='12.345.678/0001-99'
            )
            self.succes('Supermarket User and SupermarketUser created')
        else:
            self.error('Supermarket User already exists')