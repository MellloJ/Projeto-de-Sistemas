from django.test import TestCase
from django.utils.timezone import now
from users.models import ClientUser, DeliveryUser, SupermarketUser, SeparaterUser, Address
from auth_app.models import User

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class ClientUserCreateTests(APITestCase):
    def test_signup_success(self):
        data = {
            "user": {
                "email": "joao@email.com",
                "password": "123456789",
                "phone": "11987654321"
            },
            "first_name": "João",
            "last_name": "Silva",
            "cpf": "34005834132"
        }
        response = self.client.post('/users/clients/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_invalid_cpf(self):
        data = {
            "user": {
                "email": "joao@email.com",
                "password": "123456789",
                "phone": "11987654321"
            },
            "first_name": "João",
            "last_name": "Silva",
            "cpf": "11111111111"
        }
        response = self.client.post('/users/clients/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('cpf', response.data['errors'])

class ClientUserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='client@example.com', password='123')
        self.client_user = ClientUser.objects.create(user=self.user, first_name='João', last_name='Silva', cpf='12345678901')

    def test_create_client_user(self):
        self.assertEqual(ClientUser.objects.count(), 1)
        self.assertEqual(self.client_user.first_name, 'João')
        self.assertEqual(self.client_user.user.email, 'client@example.com')

    def test_update_client_user(self):
        self.client_user.first_name = 'Maria'
        self.client_user.save()
        self.assertEqual(ClientUser.objects.get(id=self.client_user.id).first_name, 'Maria')

class DeliveryUserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='delivery@example.com', password='123')
        self.delivery_user = DeliveryUser.objects.create(user=self.user, first_name='Carlos', last_name='Oliveira', cpf='23456789012')

    def test_create_delivery_user(self):
        self.assertEqual(DeliveryUser.objects.count(), 1)
        self.assertEqual(self.delivery_user.first_name, 'Carlos')
        self.assertEqual(self.delivery_user.user.email, 'delivery@example.com')

    def test_update_delivery_user(self):
        self.delivery_user.last_name = 'Souza'
        self.delivery_user.save()
        self.assertEqual(DeliveryUser.objects.get(id=self.delivery_user.id).last_name, 'Souza')

class SupermarketUserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='market@example.com', password='123')
        self.supermarket_user = SupermarketUser.objects.create(user=self.user, fantasy_name='Mercado Bom', cnpj='12345678000199')

    def test_create_supermarket_user(self):
        self.assertEqual(SupermarketUser.objects.count(), 1)
        self.assertEqual(self.supermarket_user.fantasy_name, 'Mercado Bom')
        self.assertEqual(self.supermarket_user.user.email, 'market@example.com')

    def test_update_supermarket_user(self):
        self.supermarket_user.fantasy_name = 'Mercado Top'
        self.supermarket_user.save()
        self.assertEqual(SupermarketUser.objects.get(id=self.supermarket_user.id).fantasy_name, 'Mercado Top')

class SeparaterUserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='sep@example.com', password='123')
        self.separater_user = SeparaterUser.objects.create(user=self.user, first_name='Ana', last_name='Lima', cpf='34567890123')

    def test_create_separater_user(self):
        self.assertEqual(SeparaterUser.objects.count(), 1)
        self.assertEqual(self.separater_user.first_name, 'Ana')
        self.assertEqual(self.separater_user.user.email, 'sep@example.com')

    def test_update_separater_user(self):
        self.separater_user.cpf = '99999999999'
        self.separater_user.save()
        self.assertEqual(SeparaterUser.objects.get(id=self.separater_user.id).cpf, '99999999999')

class AddressModelTests(APITestCase):
    def setUp(self):
        # Para quando tivermos as permissões bem definidas
        """ self.client.login(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.client.user) """
        self.user = User.objects.create_user(email='client@example.com', password='123456789', is_active=True)
        self.address = Address.objects.create(user=self.user, zip_code='01001-000', street='Rua Exemplo', number='123', complement='Apto 1', neighborhood='Exemplo', city='Cidade Exemplo', state='SP')
        self.assertTrue(Address.objects.filter(id=self.address.id).exists())

    def test_create_address(self):
        data = {
            "user_email": "client@example.com",
            "city": "Belo Horizonte",
            "state": "MG",
            "street": "Rua dos Ipês",
            "number": "789"
        }
        response = self.client.post('/users/addresses/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 2)
        #self.assertEqual(self.client_user.first_name, 'João')
    
    def test_get_address_user(self):
        url = reverse('address-get-by-user', kwargs={'user__email': self.user.email})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['street'], self.address.street)

    def test_get_address_one(self):
        url = reverse('address-get-one', kwargs={'pk': self.address.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['street'], self.address.street)

    def test_put_address(self):
        data = {
            "user_email": self.user.email,
            "street": "Rua Atualizada",
            "number": "456",
            "city": "Cidade Atualizada",
            "state": "RJ",
            "zip_code": "20000-000",
            "complement": "Apto 2",
            "neighborhood": "Bairro Atualizado"
        }
        url = reverse('address-edit', kwargs={'pk': self.address.id})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.address.refresh_from_db()
        self.assertEqual(self.address.street, "Rua Atualizada")
    
    def test_patch_address(self):
        data = {
            "street": "Rua Parcialmente Atualizada"
        }
        url = reverse('address-edit', kwargs={'pk': self.address.id})
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.address.refresh_from_db()
        self.assertEqual(self.address.street, "Rua Parcialmente Atualizada")
    
    def test_delete_address(self):
        url = reverse('address-delete', kwargs={'pk': self.address.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Address.objects.count(), 0)