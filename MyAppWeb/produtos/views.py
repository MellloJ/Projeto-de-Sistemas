from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views import View
from produtos.models import *

class VerProdutos(View):
    def get(self, request):
        context = {
            'title': 'Traz Aí | Produtos',
            'produtos' : Produtos.objects.all(),
            'categories' : Categorias.objects.all(),

        }
        return render(request, "produtos_index.html",context)

class VerCategorias(View):
    def get(self, request):
        context = {
            'title': 'Traz Aí | Categorias',
            'categorias': Categorias.objects.all(),
        }
        return render(request, "categorias_index.html",context)

class ImagensProdutos(View):
    def get(self, request, arquivo):
        try:
            veiculo = Produtos.objects.get(imagem='produtos/imagens/{}'.format(arquivo))
            return FileResponse(veiculo.imagem)
        except ObjectDoesNotExist:
            raise Http404('Arquivo não encontrado.')
        except Exception as exeption:
            raise exeption
        
class ImagensCategorias(View):
    def get(self, request, arquivo):
        try:
            categoria = Categorias.objects.get(imagem='produtos/categorias/{}'.format(arquivo))
            return FileResponse(categoria.imagem)
        except ObjectDoesNotExist:
            raise Http404('Arquivo não encontrado.')
        except Exception as exeption:
            raise exeption