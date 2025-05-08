from django.shortcuts import render
from django.views import View
from produtos.models import Produtos
from core.consts import CATEGORIAS_ALIMENTOS
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

class Index(View):
    def get(self, request):
        context = {
            'title': 'Traz Aí | Produtos',
            'produtos' : Produtos.objects.all(),
            'categories' : CATEGORIAS_ALIMENTOS,

        }
        return render(request, "produtos_index.html",context)

class Imagens(View):
    def get(self, request, arquivo):
        try:
            veiculo = Produtos.objects.get(imagem='produtos/imagens/{}'.format(arquivo))
            return FileResponse(veiculo.imagem)
        except ObjectDoesNotExist:
            raise Http404('Arquivo não encontrado.')
        except Exception as exeption:
            raise exeption