from produtos.services.validateSupermarketUser import usuario_e_supermarket_user
from django_dump_die.middleware import dd
from django.shortcuts import render
from django.views import View
from produtos.models import *

class Index(View):
    def get(self, request):

        if usuario_e_supermarket_user(request):
            categorias = Categorias.objects.filter(supermarket=request.user.supermarket_user)
        else:
            categorias = Categorias.objects.none()

        context = {
            'title': 'Traz Aí | Home',
            'categorias': categorias,
        }
        return render(request, "index.html",context)