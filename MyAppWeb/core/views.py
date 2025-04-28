from django_dump_die.middleware import dd
from django.shortcuts import render
from django.views import View
from core.consts import CATEGORIAS_ALIMENTOS

class Index(View):
    def get(self, request):
        context = {
            'title': 'Traz Aí | Home',
            'categories': CATEGORIAS_ALIMENTOS,
        }
        return render(request, "index.html",context)