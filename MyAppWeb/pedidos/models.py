from django.db import models
from auth_app.models import User
from users.models import ClientUser, DeliveryUser, SupermarketUser, Address
from produtos.models import Produtos

class Pedido(models.Model):
    numero_pedido = models.CharField(max_length=100, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='pedidos')
    status_pagamento = models.CharField(max_length=20, default='pendente')  # pendente, pago, etc.
    status_pedido = models.CharField(max_length=20, default='ativo')        # ativo, cancelado
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(null=True, blank=True)
    data_pagamento = models.DateTimeField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numero_pedido

class ItemPedido(models.Model):
    pedido_id = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto_id = models.ForeignKey(Produtos, on_delete=models.SET_NULL, null=True, related_name='itens_pedido')
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.produto_id.nome if self.produto_id else 'Produto indefinido'} - {self.quantidade} unidades"  

class DadosEntrega(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='dados_entrega')
    tipo_veiculo = models.CharField(max_length=50)
    endereco_id = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='entregas')

    def __str__(self):
        return f"Dados de entrega para {self.pedido_id.numero_pedido if self.pedido_id else 'Pedido indefinido'}"
