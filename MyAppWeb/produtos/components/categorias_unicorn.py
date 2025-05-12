from django_unicorn.components import UnicornView
from produtos.models import *

class CategoriasUnicornView(UnicornView):
    categorias = Categorias.objects.all()

    def mount(self):
        categorias = Categorias.objects.all()
        self.categorias = categorias.order_by('nome')

# CREATE EXTENSION IF NOT EXISTS unaccent;