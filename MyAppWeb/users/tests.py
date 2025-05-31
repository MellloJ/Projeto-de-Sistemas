from django.test import TestCase

from django.test import TestCase
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