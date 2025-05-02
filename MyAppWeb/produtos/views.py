from django.shortcuts import render
from django.views import View
from produtos.models import Produtos
from core.consts import CATEGORIAS_ALIMENTOS

class Index(View):
    def get(self, request):
        context = {
            'title': 'Traz Aí | Produtos',
            'produtos' : Produtos.objects.all(),
            'categories' : CATEGORIAS_ALIMENTOS,

        }
        return render(request, "produtos_index.html",context)