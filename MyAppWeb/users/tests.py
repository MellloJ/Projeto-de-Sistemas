from django.test import TestCase
from django.utils.timezone import now
from users.models import ClientUser, DeliveryUser, SupermarketUser, SeparaterUser
from auth_app.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from users.serializers import ClientUserSerializer

from auth_app.services.signupUser import signupClient
from auth_app.models import User

class ClientUserCreateTests(APITestCase):
    def test_signup_client_success(self):
        data = {
            "user": {
                "email": "clientusertest@example.com",
                "password": "123456789",
                "phone": "11987654321"
            },
            "first_name": "Client",
            "last_name": "Test",
            "cpf": "34005834132"
        }
        response = self.client.post('/users/clients/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_client_invalid_cpf(self):
        data = {
            "user": {
                "email": "clientusertest@example.com",
                "password": "123456789",
                "phone": "11987654321"
            },
            "first_name": "Client",
            "last_name": "Test",
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
        
class ClientUserTests(APITestCase):
    def setUp(self):
        self.clientUser, message = signupClient.register(
                    email= "clientusertest@example.com",
                    password="123456789",
                    first_name="Client",
                    last_name="Test",
                    cpf="34005834132",
                    user_type='client',
                    phone="11987654321",
                )
                   
    def test_delete_client(self):
        url = f'/users/clients/delete/{self.clientUser.user.email}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(ClientUser.objects.filter(cpf=self.clientUser.cpf).exists())
    
    def test_edit_put_client(self):
        url = f'/users/clients/edit/{self.clientUser.user.email}'
        data = {
            "user": {
                    "email": "clientusertest@example.com",
                    "password": "123456789"
            },
            'first_name': 'Client',
            'last_name': 'Fully Updated',
            'cpf': '59331091001'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['first_name'], 'Client')
        self.assertEqual(response.data['last_name'], 'Fully Updated')
        self.assertEqual(response.data['cpf'], '59331091001')
    
    def test_edit_patch_client(self):
        url = f'/users/clients/edit/{self.clientUser.user.email}'
        data = {
            'last_name': 'Partially Updated',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['last_name'], 'Partially Updated')

    def test_get_all_clients(self):
        response = self.client.get('/users/clients/get/all')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
    
    def test_get_one_client(self):
        url = f'/users/clients/get/{self.clientUser.pk}'
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['cpf'], self.clientUser.cpf)
        self.assertEqual(response.data['first_name'], self.clientUser.first_name)
        self.assertEqual(response.data['last_name'], self.clientUser.last_name)
