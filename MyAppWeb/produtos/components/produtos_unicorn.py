from django.core.exceptions import ObjectDoesNotExist
from django_unicorn.components import UnicornView
from django.db.models.functions import Lower
from django.db.models import Func
from django.urls import reverse
from produtos.models import *
import unicodedata
import json

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

    editProdutos  = {
        'wire' : "edit",
        'action': '#',
        'method': 'post',
        'id': 'editProdutos',
        'title': 'Editar Produto',
    }

    viewProdutos  = {
        'wire' : False,
        'action': '#',
        'method': 'get',
        'id': 'viewProdutos',
        'title': 'Vizualizar Produto',
    }

    createProdutos  = {
        'wire' : False,
        'action': '#',
        'method': 'post',
        'id': 'createProdutos',
        'title': 'Criar Produto',
    }

    categorias = Categorias.objects.all()

    def recarregar(self):
        if not self.usuario_e_supermarket_user():
            return
        
        produtos = Produtos.objects.filter(supermarket=self.request.user.supermarket_user)
        self.produtos = produtos.order_by('-avaliacao')

    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return ''.join([char for char in nfkd_form if not unicodedata.combining(char)])

    def mount(self):
        if not self.usuario_e_supermarket_user():
            return
        
        request = self.request
        self.categoria = request.GET.get('c')
        self.pesquisa = request.GET.get('p')
        produtos = Produtos.objects.filter(supermarket=self.request.user.supermarket_user)

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

        # self.call("loadProdutosEdit")
            
    def filter(self, data):
        if not self.usuario_e_supermarket_user():
            return
        
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            return

        categoria = data.get('categoria')
        preco_min = data.get('preco_min')
        preco_max = data.get('preco_max')
        rating = data.get('rating')

        produtos = Produtos.objects.filter(supermarket=self.request.user.supermarket_user)

        if categoria:
            produtos = produtos.filter(categoria__id=int(categoria))

        if preco_min and preco_max:
            produtos = produtos.filter(preco_unitario__gte=float(preco_min), preco_unitario__lte=float(preco_max))
        

        if rating and rating != '0':
            produtos = produtos.filter(avaliacao__gte=float(rating), avaliacao__lt=float(rating) + 1)
        
        self.produtos = produtos.order_by('-avaliacao')
        # self.call("loadProdutosEdit")

    def ordenar(self, criterio):
        if not self.usuario_e_supermarket_user():
            return
        
        try:
            criterio_data = json.loads(criterio)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            return

        order = criterio_data.get("order")
        print("Criterio de ordenação:", order)

        if order == 'relevancia':
            self.produtos = self.produtos.order_by('-avaliacao')
        elif order == 'preco':
            self.produtos = self.produtos.order_by('preco_unitario')
        
        # self.call("loadProdutosEdit")

    def usuario_e_supermarket_user(self):
        user = self.request.user
        if not user.is_authenticated:
            return False
        try:
            return hasattr(user, 'supermarket_user') and user.supermarket_user is not None
        except Exception:
            return False

# CREATE EXTENSION IF NOT EXISTS unaccent;