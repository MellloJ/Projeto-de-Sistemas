from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

class SignupAPITests(APITestCase):
    def test_signup_success(self):
        data = {
            "email": "joao@email.com",
            "password": "12345",
            "first_name": "João",
            "last_name": "Silva",
            "cpf": "34005834132",
            "phone": "11987654321"
        }
        response = self.client.post('/api/signup/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_invalid_cpf(self):
        data = {
            "email": "ana@email.com",
            "password": "12345",
            "first_name": "Ana",
            "last_name": "Souza",
            "cpf": "11111111111",
            "phone": "11987654321"
        }
        response = self.client.post('/api/signup/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('cpf', response.data['errors'])

class CreateMarketTest(APITestCase):
    def test_create_sucess(self):
        data = {
            "name": "Mercado Teste",
            "cnpj": "12345678000195",
            "phone": "11987654321",
            "email": "ribeiro.moraes@mail.uft.edu.br",
            "password": "12345"
        }

        response = self.client.post('/api/create/market/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)