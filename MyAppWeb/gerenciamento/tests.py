from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import Address, User
from django.utils.timezone import now

class AddressAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            groupName='client',
            last_login=now(),
            date_joined=now(),
            is_active=True
        )
        self.address_data = {
            'user': self.user.id,  # Usar id, não user_email
            'zip_code': '01001-000',
            'street': 'Praça da Sé',
            'number': '123',
            'complement': 'Apto 1',
            'neighborhood': 'Sé',
            'city': 'São Paulo',
            'state': 'SP',
        }
        self.address = Address.objects.create(user=self.user, zip_code='01001-000', street='Praça da Sé', number='123', complement='Apto 1', neighborhood='Sé', city='São Paulo', state='SP')

    def test_create_address(self):
        url = '/gerenciamento/api/enderecos/'
        response = self.client.post(url, self.address_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 2)
        self.assertEqual(Address.objects.last().city, 'São Paulo')
        self.assertEqual(Address.objects.last().zip_code, '01001-000')

    def test_list_addresses(self):
        url = reverse('endereco-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_address(self):
        url = reverse('endereco-detail', args=[self.address.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['city'], 'São Paulo')
        self.assertEqual(response.data['zip_code'], '01001-000')

    def test_update_address(self):
        url = f'/gerenciamento/api/enderecos/{self.address.id}/'
        data = self.address_data.copy()
        data['city'] = 'Rio de Janeiro'
        data['zip_code'] = '20000-000'
        data['user'] = self.user.id  # Usar id, não user_email
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.address.refresh_from_db()
        self.assertEqual(self.address.city, 'Rio de Janeiro')
        self.assertEqual(self.address.zip_code, '20000-000')

    def test_delete_address(self):
        url = reverse('endereco-detail', args=[self.address.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Address.objects.filter(id=self.address.id).exists())
