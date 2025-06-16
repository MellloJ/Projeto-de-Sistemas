from rest_framework.routers import SimpleRouter
from .views_api import ProdutoListCreateView, ProdutoRetrieveUpdateDestroyView, CategoriaListCreateView, CategoriaRetrieveUpdateDestroyView
from django.urls import path

router = SimpleRouter()
# Registrando rotas RESTful padrão
# router.register(r'produtos', ProdutoListCreateView, basename='produtos')
# router.register(r'categorias', CategoriaListCreateView, basename='categorias')

urlpatterns = [
    path("produtos/", ProdutoListCreateView.as_view(), name="produtos-list"),
    path("produtos/<int:pk>/", ProdutoRetrieveUpdateDestroyView.as_view(), name="produtos-detail"),
    path("categorias/", CategoriaListCreateView.as_view(), name="categorias-list"),
    path("categorias/<int:pk>/", CategoriaRetrieveUpdateDestroyView.as_view(), name="categorias-detail"),
]
# urlpatterns += router.urls