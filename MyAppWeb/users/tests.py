from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now
from users.models import ClientUser, DeliveryUser, SupermarketUser, SeparaterUser
from auth_app.models import User

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

class DeliveryUserAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='entregador1@example.com', password='123456789', is_active=True)
        self.delivery_user = DeliveryUser.objects.create(user=self.user, first_name='Entregador', last_name='Teste', cpf='50370095022')
    
    def test_api_create_delivery_user(self):
        data = {
            "user" : {
                "email" : "entregador2@example.com",
                "password" : "123456789",
                "phone" : "11987654321"
            },
            "first_name": "Entregador",
            "last_name": "Teste 2",
            "cpf": "05684811000"
        }
        response = self.client.post('/users/delivery-users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DeliveryUser.objects.count(), 2)
        self.assertEqual(DeliveryUser.objects.get(cpf="05684811000").last_name, 'Teste 2')
    
    def test_api_delete_delivery_user(self):
        url = reverse('delivery-user-delete', kwargs={'pk': self.delivery_user.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(DeliveryUser.objects.count(), 0)
    
    def test_api_get_delivery_users(self):
        url = reverse('delivery-user-get-one', kwargs={'pk': self.delivery_user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_name'], 'Teste')
    
    def test_api_put_delivery_user(self):
        url = reverse('delivery-user-edit', kwargs={'pk': self.delivery_user.id})
        data = {
            "user": {
                "email": "entregador1@example.com",
                "password": "123456789",
            },
            "first_name": "Entregador Atualizado",
            "last_name": "Teste Atualizado",
            "cpf": "50370095022",
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.delivery_user.refresh_from_db()
        self.assertEqual(self.delivery_user.first_name, 'Entregador Atualizado')
    
    def test_api_patch_delivery_user(self):
        url = reverse('delivery-user-edit', kwargs={'pk': self.delivery_user.id})
        data = {
            "last_name": "Teste Parcialmente Atualizado"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.delivery_user.refresh_from_db()
        self.assertEqual(self.delivery_user.last_name, 'Teste Parcialmente Atualizado')

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
