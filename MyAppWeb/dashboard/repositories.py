from produtos.models import Produtos
from django.db.models import Avg

def count_products(market):
    return Produtos.objects.filter(supermarket=market).count()

def average_rating(market):
    avg = Produtos.objects.filter(supermarket=market).aggregate(Avg('avaliacao'))['avaliacao__avg'] or 0.0
    return round(avg, 1)