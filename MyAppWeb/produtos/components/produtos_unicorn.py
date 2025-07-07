from django.core.exceptions import ObjectDoesNotExist
from django_unicorn.components import UnicornView
from django.db.models.functions import Lower
from django.db.models import Func
from django.urls import reverse
from produtos.models import *
from produtos.services.validateSupermarketUser import usuario_e_supermarket_user
import unicodedata
import json

class Unaccent(Func):
    function = 'unaccent'

class ProdutosUnicornView(UnicornView):
    pesquisa = None
    preco_min = None
    preco_max = None
    categoria = None
     
    produtos = None
    categorias = None


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

    def recarregar(self):
        if usuario_e_supermarket_user(self.request):
            produtos = Produtos.objects.filter(supermarket=self.request.user.supermarket_user)
            self.categorias = Categorias.objects.filter(supermarket=self.request.user.supermarket_user)
        else:
            produtos = Produtos.objects.none()
            self.categorias = Categorias.objects.none()
        self.produtos = produtos.order_by('-avaliacao')

    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return ''.join([char for char in nfkd_form if not unicodedata.combining(char)])

    def mount(self):
        if usuario_e_supermarket_user(self.request):
            self.categorias = Categorias.objects.filter(supermarket=self.request.user.supermarket_user)
            produtos = Produtos.objects.filter(supermarket=self.request.user.supermarket_user)
        else:
            self.categorias = Categorias.objects.none()
            produtos = Produtos.objects.none()
        request = self.request
        self.categoria = request.GET.get('c')
        self.pesquisa = request.GET.get('p')
        if self.categoria:
            try:
                categoria_id = int(self.categoria)
                categoria = Categorias.objects.get(id=categoria_id, supermarket=self.request.user.supermarket_user)
                produtos = produtos.filter(categoria=categoria)
            except (ObjectDoesNotExist, ValueError):
                produtos = produtos.none()
        if self.pesquisa:
            try:
                pesquisa_normalizada = self.remove_accents(self.pesquisa.lower())
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
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            return
        categoria = data.get('categoria')
        preco_min = data.get('preco_min')
        preco_max = data.get('preco_max')
        rating = data.get('rating')
        if usuario_e_supermarket_user(self.request):
            produtos = Produtos.objects.filter(supermarket=self.request.user.supermarket_user)
        else:
            produtos = Produtos.objects.none()
        if categoria:
            try:
                produtos = produtos.filter(categoria__id=int(categoria))
            except ValueError:
                produtos = produtos.none()
        if preco_min and preco_max:
            try:
                produtos = produtos.filter(preco_unitario__gte=float(preco_min), preco_unitario__lte=float(preco_max))
            except ValueError:
                produtos = produtos.none()
        if rating and rating != '0':
            try:
                rating_float = float(rating)
                produtos = produtos.filter(avaliacao__gte=rating_float, avaliacao__lt=rating_float + 1)
            except ValueError:
                produtos = produtos.none()
        self.produtos = produtos.order_by('-avaliacao')

    def ordenar(self, criterio):
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