from django.urls import path
from .views import *

urlpatterns = [
    path('create', PedidoCreateView.as_view()),                              # POST
    path('', PedidoListView.as_view()),                                      # GET (todos)
    path('<int:id>', PedidoRetrieveUpdateDeleteView.as_view()),             # GET, PATCH, DELETE
    path('<str:numeroPedido>/numeroPedido', PedidoByNumeroPedidoView.as_view()),  # GET (por número)
    path('<int:id>/cancel', PedidoCancelView.as_view()),                     # DELETE (cancelamento)
    path('<int:id>/statusPagamento', AtualizaStatusPagamentoView.as_view()), # PATCH (status)
]
