from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Produtos, Categorias
from users.models import SupermarketUser
from auth_app.models import User
from django.utils.timezone import now

class CategoriaModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(email='market@prod.com', password='123', groupName='supermarket', last_login=now(), date_joined=now())
        self.supermarket = SupermarketUser.objects.create(user=user, fantasy_name='Mercado Teste', cnpj='12345678000199')
        self.categoria = Categorias.objects.create(nome='Bebidas', descricao='Bebidas em geral', supermarket=self.supermarket)

    def test_create_categoria(self):
        self.assertEqual(Categorias.objects.count(), 1)
        self.assertEqual(self.categoria.nome, 'Bebidas')

class ProdutoModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(email='market@prod.com', password='123', groupName='supermarket', last_login=now(), date_joined=now())
        self.supermarket = SupermarketUser.objects.create(user=user, fantasy_name='Mercado Teste', cnpj='12345678000199')
        self.categoria = Categorias.objects.create(nome='Bebidas', descricao='Bebidas em geral', supermarket=self.supermarket)
        self.produto = Produtos.objects.create(nome='Coca-Cola', descricao='Refrigerante', categoria=self.categoria, marca='Coca', preco_unitario=5.99, qtd_estoque=100, codigo_barras='1234567890123', supermarket=self.supermarket)

    def test_create_produto(self):
        self.assertEqual(Produtos.objects.count(), 1)
        self.assertEqual(self.produto.nome, 'Coca-Cola')

class ProdutoAPITest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(email='market@prod.com', password='123', groupName='supermarket', last_login=now(), date_joined=now())
        self.supermarket = SupermarketUser.objects.create(user=user, fantasy_name='Mercado Teste', cnpj='12345678000199')
        self.categoria = Categorias.objects.create(nome='Bebidas', descricao='Bebidas em geral', supermarket=self.supermarket)
        self.produto = Produtos.objects.create(nome='Coca-Cola', descricao='Refrigerante', categoria=self.categoria, marca='Coca', preco_unitario=5.99, qtd_estoque=100, codigo_barras='1234567890123', supermarket=self.supermarket)

    def test_list_produtos(self):
        url = reverse('produtos-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_produto_api(self):
        url = reverse('produtos-list')
        data = {
            'nome': 'Pepsi',
            'descricao': 'Refrigerante',
            'categoria': self.categoria.id,
            'marca': 'Pepsi',
            'preco_unitario': 4.99,
            'qtd_estoque': 50,
            'codigo_barras': '9876543210987',
            'supermarket': self.supermarket.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Produtos.objects.count(), 2)
