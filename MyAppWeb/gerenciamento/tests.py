from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import Address, User, SupermarketUser
from django.contrib.auth import get_user_model
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

class DadosMercadoAPITests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='marketuser@example.com',
            password='testpass123',
            groupName='supermarket',
            last_login=now(),
            date_joined=now(),
            is_active=True
        )
        self.supermarket = SupermarketUser.objects.create(
            user=self.user,
            fantasy_name='Mercado Teste',
            cnpj='12345678000199'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_dados_mercado_by_id(self):
        url = f'/gerenciamento/api/dados-mercado/?id={self.supermarket.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['fantasy_name'], 'Mercado Teste')
        self.assertEqual(response.data['cnpj'], '12345678000199')
        self.assertEqual(response.data['email'], 'marketuser@example.com')

    def test_put_dados_mercado_update(self):
        url = '/gerenciamento/api/dados-mercado/'
        data = {
            'id': self.supermarket.id,
            'fantasy_name': 'Mercado Atualizado',
            'cnpj': '98765432000188',
            'email': 'novoemail@mercado.com',
            'phone': '11999999999'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.supermarket.refresh_from_db()
        self.assertEqual(self.supermarket.fantasy_name, 'Mercado Atualizado')
        self.assertEqual(self.supermarket.cnpj, '98765432000188')
        self.assertEqual(self.supermarket.user.email, 'novoemail@mercado.com')
        self.assertEqual(self.supermarket.user.phone, '11999999999')

    def test_get_dados_mercado_invalid_id(self):
        url = '/gerenciamento/api/dados-mercado/?id=999999'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.data)

    def test_put_dados_mercado_invalid_id(self):
        url = '/gerenciamento/api/dados-mercado/'
        data = {
            'id': 999999,
            'fantasy_name': 'Mercado Inexistente'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.data)

    def test_put_dados_mercado_missing_id(self):
        url = '/gerenciamento/api/dados-mercado/'
        data = {
            'fantasy_name': 'Sem ID'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.data)
