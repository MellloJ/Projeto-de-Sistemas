from django_dump_die.middleware import dd
from django.shortcuts import render
from django.views import View
from produtos.models import *

class Index(View):
    def get(self, request):
        context = {
            'title': 'Traz Aí | Home',
            'categorias': Categorias.objects.all(),
        }
        return render(request, "index.html",context)