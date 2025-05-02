from django.shortcuts import render
from django.views import View
from produtos.models import Produtos

class Index(View):
    def get(self, request):
        context = {
            'title': 'Traz Aí | Produtos',
            'produtos' : Produtos.objects.all(),
        }
        return render(request, "produtos_index.html",context)