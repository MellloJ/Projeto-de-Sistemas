from django.db import models

class Produtos(models.Model):
    nome = models.TextField()
    descricao = models.TextField()
    categoria = models.TextField()
    marca = models.TextField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_estoque = models.IntegerField()
    codigo_barras = models.CharField(max_length=13, unique=True)
    imagem = models.ImageField(upload_to='produtos/imagens/', blank=True, null=True)

    class Meta:
        db_table = 'produtos'
    
    def __str__(self):
        return self.nome