from django.core.exceptions import ObjectDoesNotExist
from django_unicorn.components import UnicornView
from produtos.models import *
import json

class ProdutosUnicornView(UnicornView):
    produtos = Produtos.objects.all()
    categoria: int = None
    pesquisa: str = None

    categoria = None
    preco_min = None
    preco_max = None
    categoria = None

    def mount(self):

        request = self.request
        self.categoria = request.GET.get('c')  # Exemplo: ?c=6
        self.pesquisa = request.GET.get('q')  # Exemplo: ?q=produto

        if self.categoria:
            try:
                categoria = Categorias.objects.get(id=self.categoria)
                self.produtos = Produtos.objects.filter(categoria=categoria)
            except ObjectDoesNotExist:
                self.produtos = Produtos.objects.none()
        else:
            self.produtos = Produtos.objects.all()

        if self.pesquisa:
            self.produtos = self.produtos.filter(nome__icontains=self.pesquisa)
            
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
        
        self.produtos = produtos

