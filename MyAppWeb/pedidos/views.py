from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from .models import Pedido
from users.models import User
from .serializers import PedidoSerializer

class PedidoCreateView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoListView(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    lookup_field = 'id'

class PedidoByNumeroPedidoView(APIView):
    @swagger_auto_schema(responses={200: PedidoSerializer()})
    def get(self, request, numeroPedido):
        pedido = get_object_or_404(Pedido, numero_pedido=numeroPedido)
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)

class PedidoByUserView(APIView):
    @swagger_auto_schema(responses={200: PedidoSerializer(many=True)})
    def get(self, request, user_email):
        user = User.objects.filter(email=user_email).first()
        pedidos = Pedido.objects.filter(usuario_id=user.id)
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

class PedidoCancelView(APIView):
    @swagger_auto_schema(responses={200: openapi.Response('Pedido cancelado com sucesso')})
    def delete(self, request, id):
        pedido = get_object_or_404(Pedido, id=id)
        pedido.status_pedido = 'cancelado'
        pedido.save()
        return Response({'detail': 'Pedido cancelado com sucesso'}, status=status.HTTP_200_OK)

class AtualizaStatusPagamentoView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'status_pagamento': openapi.Schema(type=openapi.TYPE_STRING, example="pago")
            },
            required=['status_pagamento']
        ),
        responses={200: PedidoSerializer()}
    )
    def patch(self, request, id):
        pedido = get_object_or_404(Pedido, id=id)
        novo_status = request.data.get('status_pagamento')
        if not novo_status:
            return Response({'error': 'Campo status_pagamento é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        pedido.status_pagamento = novo_status
        pedido.save()
        return Response(PedidoSerializer(pedido).data)
