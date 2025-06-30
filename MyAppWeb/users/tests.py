from django.test import TestCase
from django.utils.timezone import now
from users.models import ClientUser, DeliveryUser, SupermarketUser, SeparaterUser
from auth_app.models import User
from rest_framework import status

from rest_framework.test import APITestCase
from rest_framework import status

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
        self.user = User.objects.create_user(email='client@example.com', password='123', groupName='client', last_login=now(), date_joined=now())
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
        self.user = User.objects.create_user(email='delivery@example.com', password='123', groupName='delivery', last_login=now(), date_joined=now())
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
        self.user = User.objects.create_user(email='market@example.com', password='123', groupName='supermarket', last_login=now(), date_joined=now())
        self.supermarket_user = SupermarketUser.objects.create(user=self.user, fantasy_name='Mercado Bom', cnpj='12345678000199')

    def test_create_supermarket_user(self):
        self.assertEqual(SupermarketUser.objects.count(), 1)
        self.assertEqual(self.supermarket_user.fantasy_name, 'Mercado Bom')
        self.assertEqual(self.supermarket_user.user.email, 'market@example.com')

    def test_update_supermarket_user(self):
        self.supermarket_user.fantasy_name = 'Mercado Top'
        self.supermarket_user.save()
        self.assertEqual(SupermarketUser.objects.get(id=self.supermarket_user.id).fantasy_name, 'Mercado Top')

class SeparaterUserAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='separador1@example.com', password='123456789', is_active=True)
        self.separater = SeparaterUser.objects.create(user=self.user, first_name='Separador', last_name="Teste", cpf='34567890123')
    
    def test_api_create_separater_user(self):
        data = {
            "user": {
                "email": "separador2@example.com",
                "password": "123456789",
                "phone": "11987654321"
                },
            "first_name": "Separador",
            "last_name": "Teste 2",
            "cpf": "90425606066"
        }
        response = self.client.post('/users/separater-users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SeparaterUser.objects.count(), 2)
        self.assertEqual(SeparaterUser.objects.get(cpf="90425606066").last_name, 'Teste 2')
    
    def test_api_delete_separater_user(self):
        url = reverse('separater-user-delete', kwargs={'pk': self.separater.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SeparaterUser.objects.count(), 0)
    
    def test_api_get_separater_user(self):
        url = reverse('separater-user-get-one', kwargs={'pk': self.separater.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_name'], 'Teste')
    
    def test_api_put_update_separater_user(self):
        url = reverse('separater-user-edit', kwargs={'pk': self.separater.id})
        data = {
            "user": {
                "email": "separador1@example.com",
                "password": "123456789",
            },
            "first_name": "Separador Atualizado",
            "last_name": "Teste Atualizado",
            "cpf": "34567890123",
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.separater.refresh_from_db()
        self.assertEqual(self.separater.first_name, 'Separador Atualizado')
        self.assertEqual(self.separater.last_name, 'Teste Atualizado')
    
    def test_api_patch_update_separater_user(self):
        url = reverse('separater-user-edit', kwargs={'pk': self.separater.id})
        data = {
            "first_name": "Separador Parcial",
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.separater.refresh_from_db()
        self.assertEqual(self.separater.first_name, 'Separador Parcial')

class SeparaterUserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='sep@example.com', password='123', groupName='separater', last_login=now(), date_joined=now())
        self.separater_user = SeparaterUser.objects.create(user=self.user, first_name='Ana', last_name='Lima', cpf='34567890123')

    def test_create_separater_user(self):
        self.assertEqual(SeparaterUser.objects.count(), 1)
        self.assertEqual(self.separater_user.first_name, 'Ana')
        self.assertEqual(self.separater_user.user.email, 'sep@example.com')

    def test_update_separater_user(self):
        self.separater_user.cpf = '99999999999'
        self.separater_user.save()
        self.assertEqual(SeparaterUser.objects.get(id=self.separater_user.id).cpf, '99999999999')
