from django.test import TestCase
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Address
from auth_app.models import User

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

class AddressModelTests(APITestCase):
    def setUp(self):
        # Para quando tivermos as permissões bem definidas
        """ self.client.login(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.client.user) """
        self.user = User.objects.create_user(email='client@example.com', password='123456789', is_active=True)
        self.address = Address.objects.create(user=self.user, city="Cidade Exemplo", state="SP", street="Rua Exemplo", number="123")
        print(self.address)
        
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
        response = self.client.get(f'/users/addresses/get/{self.user.email}/')
        print(f"Response status: {response.status_code}")
        print(f"Response data: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['street'], self.address.street)

    def test_get_address_one(self):
        response = self.client.get(f'/users/addresses/{self.address.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['street'], self.address.street)

    def test_put_address(self):
        data = {
            "street": "Rua Atualizada",
            "number": "456",
            "city": "Cidade Atualizada",
            "state": "RJ",
            "zip_code": "87654321"
        }
        response = self.client.put(f'/users/addresses/{self.address.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.address.refresh_from_db()
        self.assertEqual(self.address.street, "Rua Atualizada")
    
    def test_patch_address(self):
        data = {
            "street": "Rua Parcialmente Atualizada"
        }
        response = self.client.patch(f'/users/addresses/{self.address.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.address.refresh_from_db()
        self.assertEqual(self.address.street, "Rua Parcialmente Atualizada")
    
    def test_delete_address(self):
        response = self.client.delete(f'/users/addresses/{self.address.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Address.objects.count(), 1)