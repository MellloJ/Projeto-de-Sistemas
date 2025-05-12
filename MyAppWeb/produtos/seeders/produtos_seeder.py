from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from produtos.models import *
import random


class CategoriasSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'CategoriasSeeder'

    def seed(self):
        try:
            categorias_data = [
                {
                    'nome': 'Grãos',
                    'descricao': 'Categoria de grãos',
                    'imagem': 'produtos/categorias/graos.svg'
                },
                {
                    'nome': 'Carnes',
                    'descricao': 'Categoria de carnes',
                    'imagem': 'produtos/categorias/carnes.svg'
                },
                {
                    'nome': 'Enlatados',
                    'descricao': 'Categoria de alimentos enlatados',
                    'imagem': 'produtos/categorias/enlatados.svg'
                },
                {
                    'nome': 'Bebidas',
                    'descricao': 'Categoria de bebidas',
                    'imagem': 'produtos/categorias/bebidas.svg'
                },
                {
                    'nome': 'Hortifruti',
                    'descricao': 'Categoria de hortifruti',
                    'imagem': 'produtos/categorias/hortifruti.svg'
                },
                {
                    'nome': 'Doces',
                    'descricao': 'Categoria de doces',
                    'imagem': 'produtos/categorias/doces.svg'
                },
                {
                    'nome': 'Laticínios',
                    'descricao': 'Categoria de laticínios',
                    'imagem': 'produtos/categorias/laticinios.svg'
                },
                {
                    'nome': 'Temperos',
                    'descricao': 'Categoria de temperos',
                    'imagem': 'produtos/categorias/temperos.svg'
                },
            ]
            for categoria in categorias_data:
                Categorias.objects.create(**categoria) 
            self.succes('Categorias seeded successfully')
        except Exception as e:
            self.error(f'Error seeding categorias: {e}')
            raise e

class ProdutosSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'ProdutosSeeder'

    def seed(self):
        try:
            produtos_data = [

                # Hortifruti
                {
                    'nome': 'Maçã Gala',
                    'descricao': 'Maçã Gala fresca e suculenta',
                    'categoria': Categorias.objects.get(nome='Hortifruti'),
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
                    'categoria': Categorias.objects.get(nome='Hortifruti'),
                    'marca': 'Natureza Pura',
                    'preco_unitario': 4.99,
                    'qtd_estoque': 150,
                    'codigo_barras': '7890123156789',
                    'imagem': 'produtos/imagens/MacaFuji.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Maçã Verde',
                    'descricao': 'Maçã Verde ácida e refrescante',
                    'categoria': Categorias.objects.get(nome='Hortifruti'),
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
                    'categoria': Categorias.objects.get(nome='Hortifruti'),
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
                    'categoria': Categorias.objects.get(nome='Hortifruti'),
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
                    'categoria': Categorias.objects.get(nome='Hortifruti'),
                    'marca': 'Natureza Pura',
                    'preco_unitario': 6.99,
                    'qtd_estoque': 100,
                    'codigo_barras': '1234567890124',
                    'imagem': 'produtos/imagens/AbacaxiPerola.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Manga Palmer',
                    'descricao': 'Manga Palmer doce e suculenta',
                    'categoria': Categorias.objects.get(nome='Hortifruti'),
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
                    'categoria': Categorias.objects.get(nome='Hortifruti'),
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
                    'categoria': Categorias.objects.get(nome='Hortifruti'),
                    'marca': 'Natureza Pura',
                    'preco_unitario': 12.99,
                    'qtd_estoque': 50,
                    'codigo_barras': '4567890123456',
                    'imagem': 'produtos/imagens/Melancia.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },

                # Bebidas
                {
                    'nome': 'Pepsi',
                    'descricao': 'pepsi geladinha',
                    'categoria': Categorias.objects.get(nome='Bebidas'),
                    'marca': 'Natureza Pura',
                    'preco_unitario': 12.99,
                    'qtd_estoque': 50,
                    'codigo_barras': '1234567890123',
                    'imagem': 'produtos/imagens/pepsi.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Fanta Laranja',
                    'descricao': 'fanta laranja geladinha',
                    'categoria': Categorias.objects.get(nome='Bebidas'),
                    'marca': 'Natureza Pura',
                    'preco_unitario': 12.99,
                    'qtd_estoque': 50,
                    'codigo_barras': '2234567890123',
                    'imagem': 'produtos/imagens/fanta_laranja.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Guaraná',
                    'descricao': 'guaraná geladinha',
                    'categoria': Categorias.objects.get(nome='Bebidas'),
                    'marca': 'Natureza Pura',
                    'preco_unitario': 12.99,
                    'qtd_estoque': 50,
                    'codigo_barras': '3234567890123',
                    'imagem': 'produtos/imagens/guarana.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Coca Cola',
                    'descricao': 'Coca Cola geladinha',
                    'categoria': Categorias.objects.get(nome='Bebidas'),
                    'marca': 'Natureza Pura',
                    'preco_unitario': 12.99,
                    'qtd_estoque': 50,
                    'codigo_barras': '4234567890123',
                    'imagem': 'produtos/imagens/coca_cola.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Guaraná Jesus',
                    'descricao': 'Guaraná Jesus geladinho e saboroso',
                    'categoria': Categorias.objects.get(nome='Bebidas'),
                    'marca': 'Natureza Pura',
                    'preco_unitario': 13.99,
                    'qtd_estoque': 60,
                    'codigo_barras': '5234567890123',
                    'imagem': 'produtos/imagens/guarana_jesus.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },

                # Grãos
                {
                    'nome': 'Arroz Integral',
                    'descricao': 'Arroz integral saudável e nutritivo',
                    'categoria': Categorias.objects.get(nome='Grãos'),
                    'marca': 'Grãos do Campo',
                    'preco_unitario': 8.99,
                    'qtd_estoque': 100,
                    'codigo_barras': '5678901234567',
                    'imagem': 'produtos/imagens/ArrozIntegral.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Feijão Preto',
                    'descricao': 'Feijão preto de alta qualidade',
                    'categoria': Categorias.objects.get(nome='Grãos'),
                    'marca': 'Grãos do Campo',
                    'preco_unitario': 6.49,
                    'qtd_estoque': 150,
                    'codigo_barras': '6789012349678',
                    'imagem': 'produtos/imagens/FeijaoPreto.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Lentilha',
                    'descricao': 'Lentilha rica em proteínas e fibras',
                    'categoria': Categorias.objects.get(nome='Grãos'),
                    'marca': 'Grãos do Campo',
                    'preco_unitario': 7.99,
                    'qtd_estoque': 120,
                    'codigo_barras': '7890123456789',
                    'imagem': 'produtos/imagens/Lentilha.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Grão de Bico',
                    'descricao': 'Grão de bico ideal para receitas saudáveis',
                    'categoria': Categorias.objects.get(nome='Grãos'),
                    'marca': 'Grãos do Campo',
                    'preco_unitario': 9.49,
                    'qtd_estoque': 80,
                    'codigo_barras': '8901234567890',
                    'imagem': 'produtos/imagens/GraoDeBico.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Quinoa',
                    'descricao': 'Quinoa orgânica e nutritiva',
                    'categoria': Categorias.objects.get(nome='Grãos'),
                    'marca': 'Grãos do Campo',
                    'preco_unitario': 12.99,
                    'qtd_estoque': 60,
                    'codigo_barras': '9012345678901',
                    'imagem': 'produtos/imagens/Quinoa.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },

                # Carnes
                {
                    'nome': 'Picanha',
                    'descricao': 'Picanha bovina de alta qualidade',
                    'categoria': Categorias.objects.get(nome='Carnes'),
                    'marca': 'Carne Premium',
                    'preco_unitario': 49.99,
                    'qtd_estoque': 50,
                    'codigo_barras': '1234567890124',
                    'imagem': 'produtos/imagens/Picanha.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Frango Inteiro',
                    'descricao': 'Frango inteiro fresco e saboroso',
                    'categoria': Categorias.objects.get(nome='Carnes'),
                    'marca': 'Carne Premium',
                    'preco_unitario': 19.99,
                    'qtd_estoque': 100,
                    'codigo_barras': '2345678901235',
                    'imagem': 'produtos/imagens/FrangoInteiro.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Costela Suína',
                    'descricao': 'Costela suína macia e saborosa',
                    'categoria': Categorias.objects.get(nome='Carnes'),
                    'marca': 'Carne Premium',
                    'preco_unitario': 29.99,
                    'qtd_estoque': 70,
                    'codigo_barras': '3456789012346',
                    'imagem': 'produtos/imagens/CostelaSuina.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Linguiça Toscana',
                    'descricao': 'Linguiça toscana ideal para churrasco',
                    'categoria': Categorias.objects.get(nome='Carnes'),
                    'marca': 'Carne Premium',
                    'preco_unitario': 15.99,
                    'qtd_estoque': 120,
                    'codigo_barras': '4567890123457',
                    'imagem': 'produtos/imagens/LinguicaToscana.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Filé de Peito de Frango',
                    'descricao': 'Filé de peito de frango fresco e saudável',
                    'categoria': Categorias.objects.get(nome='Carnes'),
                    'marca': 'Carne Premium',
                    'preco_unitario': 22.99,
                    'qtd_estoque': 90,
                    'codigo_barras': '5678901234568',
                    'imagem': 'produtos/imagens/FilePeitoFrango.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
            
                # Enlatados
                {
                    'nome': 'Milho Verde em Conserva',
                    'descricao': 'Milho verde em conserva de alta qualidade',
                    'categoria': Categorias.objects.get(nome='Enlatados'),
                    'marca': 'Conservas Premium',
                    'preco_unitario': 4.99,
                    'qtd_estoque': 200,
                    'codigo_barras': '6789012345679',
                    'imagem': 'produtos/imagens/MilhoVerde.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Ervilhas em Conserva',
                    'descricao': 'Ervilhas em conserva macias e saborosas',
                    'categoria': Categorias.objects.get(nome='Enlatados'),
                    'marca': 'Conservas Premium',
                    'preco_unitario': 5.49,
                    'qtd_estoque': 150,
                    'codigo_barras': '7890123456790',
                    'imagem': 'produtos/imagens/Ervilhas.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Atum em Óleo',
                    'descricao': 'Atum em óleo de alta qualidade',
                    'categoria': Categorias.objects.get(nome='Enlatados'),
                    'marca': 'Conservas Premium',
                    'preco_unitario': 8.99,
                    'qtd_estoque': 100,
                    'codigo_barras': '8901234567901',
                    'imagem': 'produtos/imagens/Atum.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Sardinha em Molho de Tomate',
                    'descricao': 'Sardinha em molho de tomate saboroso',
                    'categoria': Categorias.objects.get(nome='Enlatados'),
                    'marca': 'Conservas Premium',
                    'preco_unitario': 6.99,
                    'qtd_estoque': 120,
                    'codigo_barras': '9012345679012',
                    'imagem': 'produtos/imagens/Sardinha.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Tomate Pelado em Conserva',
                    'descricao': 'Tomate pelado em conserva ideal para molhos',
                    'categoria': Categorias.objects.get(nome='Enlatados'),
                    'marca': 'Conservas Premium',
                    'preco_unitario': 7.49,
                    'qtd_estoque': 80,
                    'codigo_barras': '0123456789023',
                    'imagem': 'produtos/imagens/TomatePelado.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },

                # Doces
                {
                    'nome': 'Chocolate ao Leite',
                    'descricao': 'Chocolate ao leite cremoso e delicioso',
                    'categoria': Categorias.objects.get(nome='Doces'),
                    'marca': 'Doce Sabor',
                    'preco_unitario': 5.99,
                    'qtd_estoque': 200,
                    'codigo_barras': '1234567890125',
                    'imagem': 'produtos/imagens/ChocolateAoLeite.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Bala de Goma',
                    'descricao': 'Bala de goma colorida e saborosa',
                    'categoria': Categorias.objects.get(nome='Doces'),
                    'marca': 'Doce Sabor',
                    'preco_unitario': 3.49,
                    'qtd_estoque': 300,
                    'codigo_barras': '2345678901236',
                    'imagem': 'produtos/imagens/BalaDeGoma.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Pé de Moleque',
                    'descricao': 'Pé de moleque crocante e saboroso',
                    'categoria': Categorias.objects.get(nome='Doces'),
                    'marca': 'Doce Sabor',
                    'preco_unitario': 4.99,
                    'qtd_estoque': 150,
                    'codigo_barras': '3456789012347',
                    'imagem': 'produtos/imagens/PeDeMoleque.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Doce de Leite',
                    'descricao': 'Doce de leite cremoso e artesanal',
                    'categoria': Categorias.objects.get(nome='Doces'),
                    'marca': 'Doce Sabor',
                    'preco_unitario': 6.99,
                    'qtd_estoque': 100,
                    'codigo_barras': '4567890123458',
                    'imagem': 'produtos/imagens/DoceDeLeite.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Brigadeiro',
                    'descricao': 'Brigadeiro tradicional e delicioso',
                    'categoria': Categorias.objects.get(nome='Doces'),
                    'marca': 'Doce Sabor',
                    'preco_unitario': 2.99,
                    'qtd_estoque': 250,
                    'codigo_barras': '5678901234569',
                    'imagem': 'produtos/imagens/Brigadeiro.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },

                # Laticínios
                {
                    'nome': 'Leite Integral',
                    'descricao': 'Leite integral fresco e saudável',
                    'categoria': Categorias.objects.get(nome='Laticínios'),
                    'marca': 'Laticínios Frescos',
                    'preco_unitario': 4.99,
                    'qtd_estoque': 200,
                    'codigo_barras': '6789012345680',
                    'imagem': 'produtos/imagens/LeiteIntegral.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Queijo Mussarela',
                    'descricao': 'Queijo mussarela fatiado e saboroso',
                    'categoria': Categorias.objects.get(nome='Laticínios'),
                    'marca': 'Laticínios Frescos',
                    'preco_unitario': 19.99,
                    'qtd_estoque': 100,
                    'codigo_barras': '7890123456801',
                    'imagem': 'produtos/imagens/QueijoMussarela.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Iogurte Natural',
                    'descricao': 'Iogurte natural cremoso e saudável',
                    'categoria': Categorias.objects.get(nome='Laticínios'),
                    'marca': 'Laticínios Frescos',
                    'preco_unitario': 3.49,
                    'qtd_estoque': 150,
                    'codigo_barras': '8901234567802',
                    'imagem': 'produtos/imagens/IogurteNatural.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Manteiga com Sal',
                    'descricao': 'Manteiga com sal de alta qualidade',
                    'categoria': Categorias.objects.get(nome='Laticínios'),
                    'marca': 'Laticínios Frescos',
                    'preco_unitario': 7.99,
                    'qtd_estoque': 120,
                    'codigo_barras': '9012345678903',
                    'imagem': 'produtos/imagens/ManteigaComSal.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Requeijão Cremoso',
                    'descricao': 'Requeijão cremoso ideal para pães e torradas',
                    'categoria': Categorias.objects.get(nome='Laticínios'),
                    'marca': 'Laticínios Frescos',
                    'preco_unitario': 5.49,
                    'qtd_estoque': 180,
                    'codigo_barras': '0123456789034',
                    'imagem': 'produtos/imagens/RequeijaoCremoso.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },

                # Temperos
                {
                    'nome': 'Pimenta do Reino',
                    'descricao': 'Pimenta do reino moída de alta qualidade',
                    'categoria': Categorias.objects.get(nome='Temperos'),
                    'marca': 'Especiarias Finas',
                    'preco_unitario': 3.99,
                    'qtd_estoque': 200,
                    'codigo_barras': '1234567890126',
                    'imagem': 'produtos/imagens/PimentaDoReino.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Orégano',
                    'descricao': 'Orégano seco e aromático',
                    'categoria': Categorias.objects.get(nome='Temperos'),
                    'marca': 'Especiarias Finas',
                    'preco_unitario': 2.49,
                    'qtd_estoque': 300,
                    'codigo_barras': '2345678901237',
                    'imagem': 'produtos/imagens/Oregano.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Colorau',
                    'descricao': 'Colorau natural para dar cor e sabor',
                    'categoria': Categorias.objects.get(nome='Temperos'),
                    'marca': 'Especiarias Finas',
                    'preco_unitario': 4.99,
                    'qtd_estoque': 150,
                    'codigo_barras': '3456789012348',
                    'imagem': 'produtos/imagens/Colorau.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Cominho',
                    'descricao': 'Cominho moído com aroma intenso',
                    'categoria': Categorias.objects.get(nome='Temperos'),
                    'marca': 'Especiarias Finas',
                    'preco_unitario': 3.49,
                    'qtd_estoque': 120,
                    'codigo_barras': '4567890123459',
                    'imagem': 'produtos/imagens/Cominho.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
                {
                    'nome': 'Páprica Doce',
                    'descricao': 'Páprica doce para realçar o sabor dos pratos',
                    'categoria': Categorias.objects.get(nome='Temperos'),
                    'marca': 'Especiarias Finas',
                    'preco_unitario': 5.49,
                    'qtd_estoque': 180,
                    'codigo_barras': '5678901234570',
                    'imagem': 'produtos/imagens/PapricaDoce.jpeg',
                    'qtd_avaliacoes': random.randint(0, 500),
                    'avaliacao': round(random.uniform(1, 5), 1)
                },
            ]

            # Conjunto para rastrear códigos de barras únicos
            codigos_barras_usados = set()

            for produto_data in produtos_data:
                codigo_barras = produto_data['codigo_barras']
                while codigo_barras in codigos_barras_usados:
                    # Gera um novo código de barras único
                    codigo_barras = str(random.randint(1000000000000, 9999999999999))
                produto_data['codigo_barras'] = codigo_barras
                codigos_barras_usados.add(codigo_barras)

                Produtos.objects.create(**produto_data)

            self.succes('Produtos seeded successfully')
        except Exception as e:
            self.error(f'Error seeding produtos: {e}')
            raise e