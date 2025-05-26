from produtos.services.validateSupermarketUser import usuario_e_supermarket_user
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect
from django_dump_die.middleware import dd
from produtos.forms import ProdutosForm
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from produtos.models import *
from pathlib import Path
import json

class ProdutosView(View):
    def get(self, request, *args, **kwargs):
        
        breadcrumbs = [
            {'name': 'Produtos'},
        ]

        filterModal = {
            'wire' : 'filter',
            'action': '#',
            'method': 'get',
            'id': 'filterModal',
            'title': 'Filtro',
        }

        if usuario_e_supermarket_user(request):
            categorias = Categorias.objects.filter(supermarket=request.user.supermarket_user)
        else:
            categorias = Categorias.objects.none()

        context = {
            'title': 'Traz Aí | Produtos',
            'categorias' : categorias,
            'breadcrumbs' : breadcrumbs,
            'filterModal' : filterModal,
        }

        return render(request, "produtos/index.html",context)

class CategoriasView(View):
    def get(self, request):

        breadcrumbs = [
            {'name': 'Categorias'},
        ]

        if usuario_e_supermarket_user(request):
            categorias = Categorias.objects.filter(supermarket=request.user.supermarket_user)
        else:
            categorias = Categorias.objects.none()

        context = {
            'title': 'Traz Aí | Categorias',
            'categorias': categorias,
            'breadcrumbs' :breadcrumbs,
        }
        return render(request, "categorias/index.html",context)

class ImagensProdutosView(View):
    def get(self, request, arquivo):
        try:
            try:
                produto = Produtos.objects.get(
                    imagem='produtos/imagens/{}'.format(arquivo),
                )
                file_path = Path(produto.imagem.path)
                if file_path.is_file():
                    return FileResponse(file_path.open('rb'))
                else:
                    empty_image_path = Path('static/src/produtos/img/empty.svg')
                    return FileResponse(empty_image_path.open('rb'))
            except ObjectDoesNotExist:
                raise Http404('Arquivo não encontrado.')
        except ObjectDoesNotExist:
            raise Http404('Arquivo não encontrado.')
        except Exception as exeption:
            raise exeption
        
class ImagensCategoriasView(View):
    def get(self, request, arquivo):
        try:
            try:
                categoria = Categorias.objects.get(
                    imagem='produtos/categorias/{}'.format(arquivo),
                )
                file_path = Path(categoria.imagem.path)
                if file_path.is_file():
                    return FileResponse(file_path.open('rb'))
                else:
                    empty_image_path = Path('static/src/produtos/img/empty.svg')
                    return FileResponse(empty_image_path.open('rb'))
            except ObjectDoesNotExist:
                raise Http404('Arquivo não encontrado.')
        except ObjectDoesNotExist:
            raise Http404('Arquivo não encontrado.')
        except Exception as exeption:
            raise exeption
        
class FilterView(View):
    def get(self, request):
        filter = request.GET.dict()

        if usuario_e_supermarket_user(request):
            produtos = Produtos.objects.filter(supermarket=request.user.supermarket_user)
        else:
            produtos = Produtos.objects.none()

        if filter.get('categoria'):
            try:
                produtos = produtos.filter(categoria__id=filter.get('categoria'))
            except ObjectDoesNotExist:
                pass

        if filter.get('preco-min') and filter.get('preco-max'):
            try:
                produtos = produtos.filter(preco_unitario__gte=filter.get('preco-min'), preco_unitario__lte=filter.get('preco-max'))
            except ObjectDoesNotExist:
                pass

        if filter.get('rating') and filter.get('rating') != '0':
            try:
                float_filter = float(filter.get('rating'))
                produtos = produtos.filter(avaliacao__gte=float_filter, avaliacao__lt=float_filter + 1)
            except ValueError:
                pass

        produtos_data = list(produtos.values())

        return JsonResponse({'produtos': produtos_data})
