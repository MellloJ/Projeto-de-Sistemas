from rest_framework import serializers
from .models import Pedido, ItemPedido, DadosEntrega

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        exclude = ['pedido_id']  # Não exigimos isso do usuário

class DadosEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosEntrega
        exclude = ['pedido_id']  # Também será atribuído automaticamente

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, required=False)
    dados_entrega = DadosEntregaSerializer(many=True, required=False)

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        itens_data = validated_data.pop('itens', [])
        entrega_data = validated_data.pop('dados_entrega', [])
        pedido = Pedido.objects.create(**validated_data)

        for item in itens_data:
            ItemPedido.objects.create(pedido_id=pedido, **item)

        for entrega in entrega_data:
            DadosEntrega.objects.create(pedido_id=pedido, **entrega)

        return pedido

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
