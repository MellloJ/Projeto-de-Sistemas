from rest_framework import serializers
from .models import Produtos, Categorias

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = [
            'id', 
            'nome', 
            'descricao', 
            'preco_unitario', 
            'categoria', 
            'marca', 
            'qtd_estoque', 
            'codigo_barras', 
            'qtd_avaliacoes', 
            'avaliacao', 
            'imagem',
            'supermarket'
        ]