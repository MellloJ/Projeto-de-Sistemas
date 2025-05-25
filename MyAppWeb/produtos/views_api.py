from rest_framework import generics
from .models import Produtos, Categorias
from .serializers import ProdutoSerializer, CategoriaSerializer

class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer

class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer