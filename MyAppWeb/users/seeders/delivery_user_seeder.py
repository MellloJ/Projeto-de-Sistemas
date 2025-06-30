from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from django.contrib.auth import get_user_model
from django.utils.timezone import now

class DeliveryUserSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'DeliveryUserSeeder'
    
    def seed(self):
        from users.models import DeliveryUser
        User = get_user_model()
        if not User.objects.filter(email='deliver@example.com').exists():
            user = User.objects.create_user(
                email='deliver@example.com',
                password='123456789',
                user_type='delivery',
                is_active=True
            )
            DeliveryUser.objects.create(
                user=user,
                first_name='Entregador',
                last_name='Teste',
                cpf='50370095022',
            )
            self.succes('Delivery User and DeliveryUser created')
        else:
            self.error('Delivery User already exists')