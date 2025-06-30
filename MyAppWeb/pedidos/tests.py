from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Pedido, ItemPedido
from produtos.models import Produtos, Categorias
from users.models import ClientUser, SupermarketUser
from auth_app.models import User
from django.utils.timezone import now

class PedidoModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(email='client@pedido.com', password='123', user_type='client', )
        self.client_user = ClientUser.objects.create(user=user, first_name='Cliente', last_name='Teste', cpf='12345678901')
        market_user = User.objects.create_user(email='market@pedido.com', password='123', user_type='supermarket', )
        self.supermarket = SupermarketUser.objects.create(user=market_user, fantasy_name='Mercado Pedido', cnpj='12345678000199')
        self.categoria = Categorias.objects.create(nome='Bebidas', descricao='Bebidas', supermarket=self.supermarket)
        self.produto = Produtos.objects.create(nome='Coca-Cola', descricao='Refrigerante', categoria=self.categoria, marca='Coca', preco_unitario=5.99, qtd_estoque=100, codigo_barras='1234567890123', supermarket=self.supermarket)
        self.pedido = Pedido.objects.create(numero_pedido='PED123', usuario=user, valor_total=5.99)
        self.item = ItemPedido.objects.create(pedido_id=self.pedido, produto_id=self.produto, quantidade=1, preco_unitario=5.99)

    def test_create_pedido(self):
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(ItemPedido.objects.count(), 1)

class PedidoAPITest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(email='client@pedido.com', password='123', user_type='client')
        self.client_user = ClientUser.objects.create(user=user, first_name='Cliente', last_name='Teste', cpf='12345678901')
        market_user = User.objects.create_user(email='market@pedido.com', password='123', user_type='supermarket', )
        self.supermarket = SupermarketUser.objects.create(user=market_user, fantasy_name='Mercado Pedido', cnpj='12345678000199')
        self.categoria = Categorias.objects.create(nome='Bebidas', descricao='Bebidas', supermarket=self.supermarket)
        self.produto = Produtos.objects.create(nome='Coca-Cola', descricao='Refrigerante', categoria=self.categoria, marca='Coca', preco_unitario=5.99, qtd_estoque=100, codigo_barras='1234567890123', supermarket=self.supermarket)
        self.pedido = Pedido.objects.create(numero_pedido='PED123', usuario=user, valor_total=5.99)
        self.item = ItemPedido.objects.create(pedido_id=self.pedido, produto_id=self.produto, quantidade=1, preco_unitario=5.99)

    def test_list_pedidos(self):
        url = reverse('pedidos-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pedido_api(self):
        url = reverse('pedidos-list')
        data = {
            'numero_pedido': 'PED456',
            'usuario': self.pedido.usuario.id,
            'valor_total': 10.00,
            'status_pagamento': 'pendente',
            'status_pedido': 'ativo',
            'itens': [
                {
                    'produto_id': self.produto.id,
                    'quantidade': 2,
                    'preco_unitario': 5.00,
                    'disponibilidade': True
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Pedido.objects.count(), 2)
    
    def test_api_get_pedido_by_user(self):
        url = reverse('pedidos-by-user', args=[self.client_user.user.email])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertIsInstance(response.data, list)
