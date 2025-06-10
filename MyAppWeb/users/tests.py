from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from users.models import ClientUser
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