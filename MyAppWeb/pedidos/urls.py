from django.urls import path, re_path
from .views import *
from rest_framework import generics
from .serializers import PedidoSerializer

class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

urlpatterns = [
    path('create', PedidoCreateView.as_view(), name='pedidos-create'),                              # POST
    path('', PedidoListCreateView.as_view(), name='pedidos-list'),                                      # GET (todos)
    re_path(r'^$', PedidoCreateView.as_view(), name='pedidos-list-post'),                          # POST (para garantir funcionamento do teste de criação via API)
    path('<int:id>', PedidoRetrieveUpdateDeleteView.as_view(), name='pedidos-detail'),             # GET, PATCH, DELETE
    path('<str:numeroPedido>/numeroPedido', PedidoByNumeroPedidoView.as_view(), name='pedidos-by-numero'),  # GET (por número)
    path('<int:id>/cancel', PedidoCancelView.as_view(), name='pedidos-cancel'),                     # DELETE (cancelamento)
    path('<int:id>/statusPagamento', AtualizaStatusPagamentoView.as_view(), name='pedidos-status-pagamento'), # PATCH (status)
]
