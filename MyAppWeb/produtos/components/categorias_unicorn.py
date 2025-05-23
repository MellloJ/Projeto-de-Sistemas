from django_unicorn.components import UnicornView
from django.urls import reverse
from produtos.models import *

class CategoriasUnicornView(UnicornView):
    categorias = Categorias.objects.all()

    createCategorias = {
        'wire': False,
        'action': reverse('categorias'),
        'method': 'post',
        'id': 'createCategorias',
        'title': 'Criar Categoria',
    }

    def mount(self):
        categorias = Categorias.objects.all()
        self.categorias = categorias.order_by('nome')

# CREATE EXTENSION IF NOT EXISTS unaccent;