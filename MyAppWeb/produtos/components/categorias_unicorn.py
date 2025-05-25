from django_unicorn.components import UnicornView
from django.urls import reverse
from produtos.models import *

class CategoriasUnicornView(UnicornView):
    categorias = Categorias.objects.all()

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
        categorias = Categorias.objects.all()
        self.categorias = categorias.order_by('nome')

    def mount(self):
        categorias = Categorias.objects.all()
        self.categorias = categorias.order_by('nome')

# CREATE EXTENSION IF NOT EXISTS unaccent;