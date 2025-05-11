from django.urls import path, include
from produtos.views import *


urlpatterns = [
    path('api/', include('produtos.urls_api')),
    path('visao', ProdutosView.as_view(), name='produtos'),
    path('categorias', CategoriasView.as_view(), name='categorias'),
    path('filter', FilterView.as_view(), name='filter'),
    path('imagens/<str:arquivo>', ImagensProdutosView.as_view(), name='imagens_produtos'),
    path('categorias/<str:arquivo>', ImagensCategoriasView.as_view(), name='imagens_categorias'),
]