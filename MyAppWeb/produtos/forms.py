from django import forms

from django import forms
from produtos.models import *  
class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'descricao', 'categoria', 'marca', 'preco_unitario', 'qtd_estoque', 'codigo_barras', 'imagem', 'supermarket']
