from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from produtos.models import Produtos
import random

class ProdutosSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'ProdutosSeeder'

    def seed(self):
        try:
            produtos_data = [
                {
                    'nome': 'Maçã Gala',
                    'descricao': 'Maçã Gala fresca e suculenta',
                    'categoria': 'Frutas',
                    'marca': 'Natureza Pura',
                    'preco_unitario': 3.99,
                    'qtd_estoque': 200,
                    'codigo_barras': '6789012345678',
                    'imagem': 'produtos/imagens/MacaGala.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Maçã Fuji',
                    'descricao': 'Maçã Fuji doce e crocante',
                    'categoria': 'Frutas',
                    'marca': 'Natureza Pura',
                    'preco_unitario': 4.99,
                    'qtd_estoque': 150,
                    'codigo_barras': '7890123456789',
                    'imagem': 'produtos/imagens/MacaFuji.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Maçã Verde',
                    'descricao': 'Maçã Verde ácida e refrescante',
                    'categoria': 'Frutas',
                    'marca': 'Natureza Pura',
                    'preco_unitario': 5.49,
                    'qtd_estoque': 120,
                    'codigo_barras': '8901234567890',
                    'imagem': 'produtos/imagens/MacaVerde.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Banana Prata',
                    'descricao': 'Banana Prata madura e saborosa',
                    'categoria': 'Frutas',
                    'marca': 'Natureza Pura',
                    'preco_unitario': 2.99,
                    'qtd_estoque': 300,
                    'codigo_barras': '9012345678901',
                    'imagem': 'produtos/imagens/BananaPrata.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Laranja Pera',
                    'descricao': 'Laranja Pera doce e suculenta',
                    'categoria': 'Frutas',
                    'marca': 'Natureza Pura',
                    'preco_unitario': 3.49,
                    'qtd_estoque': 250,
                    'codigo_barras': '0123456789012',
                    'imagem': 'produtos/imagens/LaranjaPera.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Abacaxi Pérola',
                    'descricao': 'Abacaxi Pérola doce e refrescante',
                    'categoria': 'Frutas',
                    'marca': 'Natureza Pura',
                    'preco_unitario': 6.99,
                    'qtd_estoque': 100,
                    'codigo_barras': '1234567890123',
                    'imagem': 'produtos/imagens/AbacaxiPerola.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Manga Palmer',
                    'descricao': 'Manga Palmer doce e suculenta',
                    'categoria': 'Frutas',
                    'marca': 'Natureza Pura',
                    'preco_unitario': 4.49,
                    'qtd_estoque': 180,
                    'codigo_barras': '2345678901234',
                    'imagem': 'produtos/imagens/MangaPalmer.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Uva Thompson',
                    'descricao': 'Uva Thompson sem sementes e doce',
                    'categoria': 'Frutas',
                    'marca': 'Natureza Pura',
                    'preco_unitario': 7.99,
                    'qtd_estoque': 90,
                    'codigo_barras': '3456789012345',
                    'imagem': 'produtos/imagens/UvaThompson.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Melancia',
                    'descricao': 'Melancia fresca e suculenta',
                    'categoria': 'Frutas',
                    'marca': 'Natureza Pura',
                    'preco_unitario': 12.99,
                    'qtd_estoque': 50,
                    'codigo_barras': '4567890123456',
                    'imagem': 'produtos/imagens/Melancia.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
            ]
            for produto_data in produtos_data:
                Produtos.objects.create(**produto_data) 
            self.succes('Produtos seeded successfully')
        except Exception as e:
            self.error(f'Error seeding produtos: {e}')
            raise e