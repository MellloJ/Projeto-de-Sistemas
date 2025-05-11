from django.core.exceptions import ObjectDoesNotExist
from django_unicorn.components import UnicornView
from produtos.models import *
import unicodedata
import json
from django.db.models.functions import Lower
from django.db.models import Func

class Unaccent(Func):
    function = 'unaccent'

class ProdutosUnicornView(UnicornView):
    pesquisa = None
    produtos = None
    categoria = None
    categoria = None
    preco_min = None
    preco_max = None
    categoria = None

    editModal  = {
        'wire' : "edit",
        'action': '#',
        'method': 'post',
        'id': 'editModal',
        'title': 'Editar Produto',
    }

    viewModal  = {
        'wire' : "edit",
        'action': '#',
        'method': 'get',
        'id': 'viewModal',
        'title': 'Vizualizar Produto',
    }

    categorias = Categorias.objects.all()

    def recarregar(self):
        produtos = Produtos.objects.all()
        self.produtos = produtos.order_by('-avaliacao')

    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return ''.join([char for char in nfkd_form if not unicodedata.combining(char)])

    def mount(self):
        request = self.request
        self.categoria = request.GET.get('c')
        self.pesquisa = request.GET.get('p')
        produtos = Produtos.objects.all()

        print("Categoria:", self.categoria)
        print("Pesquisa:", self.pesquisa)

        if self.categoria:
            try:
                categoria = Categorias.objects.get(id=self.categoria)
                produtos = produtos.filter(categoria=categoria)
            except ObjectDoesNotExist:
                produtos = produtos.none()

        if self.pesquisa:
            try:
                # Normalize the search query
                pesquisa_normalizada = self.remove_accents(self.pesquisa.lower())

                # Annotate and normalize the database field
                produtos = produtos.annotate(
                    nome_normalizado=Unaccent(Lower('nome'))
                ).filter(
                    nome_normalizado__icontains=pesquisa_normalizada
                )
            except Exception as e:
                print("Error during search filtering:", e)
                produtos = produtos.none()

        produtos = produtos.order_by('-avaliacao')
        self.produtos = produtos
            
    def filter(self, data):
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            return

        categoria = data.get('categoria')
        preco_min = data.get('preco_min')
        preco_max = data.get('preco_max')
        rating = data.get('rating')

        produtos = Produtos.objects.all()

        if categoria:
            produtos = produtos.filter(categoria__id=int(categoria))

        if preco_min and preco_max:
            produtos = produtos.filter(preco_unitario__gte=float(preco_min), preco_unitario__lte=float(preco_max))
        

        if rating and rating != '0':
            produtos = produtos.filter(avaliacao__gte=float(rating), avaliacao__lt=float(rating) + 1)
        
        self.produtos = produtos.order_by('-avaliacao')
        self.call("loadProdutosView")
        self.call("loadProdutosEdit")

# CREATE EXTENSION IF NOT EXISTS unaccent;