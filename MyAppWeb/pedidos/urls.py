from django.urls import path
from .views import *

urlpatterns = [
    path('pedido/create', PedidoCreateView.as_view()),                              # POST
    path('pedido/', PedidoListView.as_view()),                                      # GET (todos)
    path('pedido/<int:id>', PedidoRetrieveUpdateDeleteView.as_view()),             # GET, PATCH, DELETE
    path('pedido/<str:numeroPedido>/numeroPedido', PedidoByNumeroPedidoView.as_view()),  # GET (por número)
    path('pedido/<int:id>/cancel', PedidoCancelView.as_view()),                     # DELETE (cancelamento)
    path('pedido/<int:id>/statusPagamento', AtualizaStatusPagamentoView.as_view()), # PATCH (status)
]
