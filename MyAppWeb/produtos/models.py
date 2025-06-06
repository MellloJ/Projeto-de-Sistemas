from django.db import models
from django.conf import settings
from users.models import SupermarketUser

class Categorias(models.Model):
    nome = models.TextField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/categorias/', blank=True, null=True)
    supermarket = models.ForeignKey(SupermarketUser, on_delete=models.SET_NULL, null=True, related_name='categorias')

    class Meta:
        db_table = 'categorias'
    
    def __str__(self):
        return self.nome
    
class Produtos(models.Model):
    nome = models.TextField()
    descricao = models.TextField()
    categoria = models.ForeignKey('Categorias', on_delete=models.SET_NULL, null=True, related_name='produtos')
    marca = models.TextField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_estoque = models.IntegerField()
    codigo_barras = models.CharField(max_length=13, unique=True)
    qtd_avaliacoes = models.IntegerField(default=0)
    avaliacao = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    imagem = models.ImageField(upload_to='produtos/imagens/', blank=True, null=True)
    supermarket = models.ForeignKey(SupermarketUser, on_delete=models.SET_NULL, null=True, related_name='produtos')

    class Meta:
        db_table = 'produtos'
    
    def __str__(self):
        return self.nome
    
class Avaliacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)
    produto = models.ForeignKey('Produtos', on_delete=models.SET_NULL, null=True, related_name='avaliacoes')
    nota = models.IntegerField()

    class Meta:
        db_table = 'avaliacoes'
    
    def __str__(self):
        return f'{self.produto.nome} : {self.nota}'