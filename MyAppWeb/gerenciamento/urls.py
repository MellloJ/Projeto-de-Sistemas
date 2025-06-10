from django.urls import path, include
from gerenciamento.views import *


urlpatterns = [
    path('usuarios/', Usuarios.as_view(), name='gerenciamento_usuarios'),
    path('dados-mercado/', DadosMercado.as_view(), name='gerenciamento_dados_mercado'),
    path('enderecos/', Enderecos.as_view(), name='gerenciamento_enderecos'),
    path('documentos/', Documentos.as_view(), name='gerenciamento_documentos'),
    path('servicos/', Servicos.as_view(), name='gerenciamento_servicos'),
    # Inclui as rotas da API REST
    path('api/', include('gerenciamento.urls_api')),
]