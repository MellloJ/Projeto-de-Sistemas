from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django_dump_die.middleware import dd
from produtos.forms import ProdutosForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from produtos.models import *

class ProdutosView(View):
    def get(self, request):
        breadcrumbs = [
            {'name': 'Produtos'},
        ]

        filterModal = {
            'action': '#',
            'method': 'get',
            'id': 'filterModal',
            'title': 'Filtro',
        }

        createModal  = {
            'action': reverse('produtos'),
            'method': 'post',
            'id': 'createModal',
            'title': 'Criar Produto',
        }

        context = {
            'title': 'Traz Aí | Produtos',
            'produtos' : Produtos.objects.all(),
            'categorias' : Categorias.objects.all(),
            'breadcrumbs' : breadcrumbs,
            'filterModal' : filterModal,
            'createModal' : createModal,

        }

        return render(request, "produtos/index.html",context)
    
    def post(self, request):
        form = ProdutosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produtos')
        else:
            return redirect('produtos')

class CategoriasView(View):
    def get(self, request):

        breadcrumbs = [
            {'name': 'Categorias'},
        ]

        context = {
            'title': 'Traz Aí | Categorias',
            'categorias': Categorias.objects.all(),
            'breadcrumbs' :breadcrumbs,
        }
        return render(request, "categorias/index.html",context)

class ImagensProdutosView(View):
    def get(self, request, arquivo):
        try:
            veiculo = Produtos.objects.get(imagem='produtos/imagens/{}'.format(arquivo))
            return FileResponse(veiculo.imagem)
        except ObjectDoesNotExist:
            raise Http404('Arquivo não encontrado.')
        except Exception as exeption:
            raise exeption
        
class ImagensCategoriasView(View):
    def get(self, request, arquivo):
        try:
            categoria = Categorias.objects.get(imagem='produtos/categorias/{}'.format(arquivo))
            return FileResponse(categoria.imagem)
        except ObjectDoesNotExist:
            raise Http404('Arquivo não encontrado.')
        except Exception as exeption:
            raise exeption