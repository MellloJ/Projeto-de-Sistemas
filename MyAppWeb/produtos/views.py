from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        context = {
            'title': 'Traz Aí | Produtos',
        }
        return render(request, "produtos_index.html",context)