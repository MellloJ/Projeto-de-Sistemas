from django.urls import path
from produtos import views


urlpatterns = [
    path('visao', views.ProdutosView.as_view(), name='produtos'),
    path('categorias', views.CategoriasView.as_view(), name='categorias'),
    path('imagens/<str:arquivo>', views.ImagensProdutosView.as_view(), name='imagens_produtos'),
    path('categorias/<str:arquivo>', views.ImagensCategoriasView.as_view(), name='imagens_categorias'),
]