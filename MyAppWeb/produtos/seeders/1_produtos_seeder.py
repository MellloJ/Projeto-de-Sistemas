from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from produtos.models import Produtos

class ProdutosSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'ProdutosSeeder'

    def seed(self):
        try:
            produtos_data = [
                {
                    'nome': 'Produto 1',
                    'descricao': 'Descrição do Produto 1',
                    'categoria': 'Categoria 1',
                    'marca': 'Marca 1',
                    'preco_unitario': 10.99,
                    'qtd_estoque': 100,
                    'codigo_barras': '1234567890123',
                    'imagem': None
                },
                {
                    'nome': 'Produto 2',
                    'descricao': 'Descrição do Produto 2',
                    'categoria': 'Categoria 2',
                    'marca': 'Marca 2',
                    'preco_unitario': 20.99,
                    'qtd_estoque': 50,
                    'codigo_barras': '2345678901234',
                    'imagem': None
                },
                {
                    'nome': 'Produto 3',
                    'descricao': 'Descrição do Produto 3',
                    'categoria': 'Categoria 3',
                    'marca': 'Marca 3',
                    'preco_unitario': 30.99,
                    'qtd_estoque': 75,
                    'codigo_barras': '3456789012345',
                    'imagem': None
                },
                {
                    'nome': 'Produto 4',
                    'descricao': 'Descrição do Produto 4',
                    'categoria': 'Categoria 4',
                    'marca': 'Marca 4',
                    'preco_unitario': 40.99,
                    'qtd_estoque': 75,
                    'codigo_barras': '4456789012445',
                    'imagem': None
                },
                {
                    'nome': 'Produto 5',
                    'descricao': 'Descrição do Produto 5',
                    'categoria': 'Categoria 5',
                    'marca': 'Marca 5',
                    'preco_unitario': 50.99,
                    'qtd_estoque': 75,
                    'codigo_barras': '5456789012545',
                    'imagem': None
                }
            ]
            for produto_data in produtos_data:
                Produtos.objects.create(**produto_data) 
            self.succes('Produtos seeded successfully')
        except Exception as e:
            self.error(f'Error seeding produtos: {e}')
            raise e