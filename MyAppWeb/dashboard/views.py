from django.shortcuts import render
from django.views import View
from dashboard.repositories import count_products, average_rating

# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        breadcrumbs = [
            {'name': 'Dashboard'},
        ]

        market = request.user.supermarket_user if request.user.is_authenticated and hasattr(request.user, 'supermarket_user') else 0

        context = {
            'title': 'Traz Aí | Dashboard',
            'breadcrumbs': breadcrumbs,
            'qtd_produtos': count_products(market),
            'avaliacao': average_rating(market),
        }

        return render(request, "dashboard/index.html", context)
