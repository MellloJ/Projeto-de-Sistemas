from django_unicorn.components import UnicornView
from django.urls import reverse
from produtos.models import *
from produtos.services.validateSupermarketUser import usuario_e_supermarket_user

class CategoriasUnicornView(UnicornView):
    categorias = None

    editCategorias  = {
        'wire' : "edit",
        'action': '#',
        'method': 'post',
        'id': 'editCategorias',
        'title': 'Editar Categorias',
    }

    viewCategorias  = {
        'wire' : False,
        'action': '#',
        'method': 'get',
        'id': 'viewCategorias',
        'title': 'Vizualizar Categorias',
    }

    createCategorias = {
        'wire': False,
        'action': '#',
        'method': 'post',
        'id': 'createCategorias',
        'title': 'Criar Categoria',
    }

    def recarregar(self):
        if usuario_e_supermarket_user(self.request):
            categorias = Categorias.objects.filter(supermarket=self.request.user.supermarket_user)
        else:
            categorias = Categorias.objects.none()
        self.categorias = categorias.order_by('nome')

    def mount(self):
        if usuario_e_supermarket_user(self.request):
            categorias = Categorias.objects.filter(supermarket=self.request.user.supermarket_user)
        else:
            categorias = Categorias.objects.none()
        self.categorias = categorias.order_by('nome')

# CREATE EXTENSION IF NOT EXISTS unaccent;