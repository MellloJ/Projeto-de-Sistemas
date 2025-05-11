from django.urls import path
from .views_api import *

urlpatterns = [
    path("produtos/", ProdutoListCreateView.as_view(), name="produto-list-create"),
    path("editar/<int:pk>", ProdutoRetrieveUpdateDestroyView.as_view(), name="produto-editar"),
]