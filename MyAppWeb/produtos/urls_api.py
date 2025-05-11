from django.urls import path
from .views_api import ProdutoListCreateView

urlpatterns = [
    path("produtos/", ProdutoListCreateView.as_view(), name="produto-list-create"),
]