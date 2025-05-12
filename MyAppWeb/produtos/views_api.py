from rest_framework import generics
from .models import Produtos
from .serializers import ProdutoSerializer

class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer