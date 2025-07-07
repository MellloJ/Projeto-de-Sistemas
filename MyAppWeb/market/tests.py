from rest_framework.test import APITestCase
from rest_framework import status

class CreateMarketTest(APITestCase):
    def test_create_sucess(self):
        data = {
            "name": "Mercado Teste",
            "cnpj": "12345678000195",
            "phone": "11987654321",
            "email": "mercado1@gmail.com",
            "password": "12345"
        }

        response = self.client.post('/api/create/market', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)