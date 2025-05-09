from django.urls import path
from produtos import views


urlpatterns = [
    path('visao', views.VerProdutos.as_view(), name='produtos'),
    path('categorias', views.VerCategorias.as_view(), name='categorias'),
    path('imagens/<str:arquivo>', views.ImagensProdutos.as_view(), name='imagens_produtos'),
    path('categorias/<str:arquivo>', views.ImagensCategorias.as_view(), name='imagens_categorias'),
]