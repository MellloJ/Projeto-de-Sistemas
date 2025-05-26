from django.urls import path
from .views_api import *

urlpatterns = [
    path("produtos/", ProdutoListCreateView.as_view(), name="produto-list-create"),
    path("editar/produto/<int:pk>", ProdutoRetrieveUpdateDestroyView.as_view(), name="produto-editar"),
    path("categorias/", CategoriaListCreateView.as_view(), name="categoria-list-create"),
    path("editar/categoria/<int:pk>", CategoriaRetrieveUpdateDestroyView.as_view(), name="categoria-editar"),
]