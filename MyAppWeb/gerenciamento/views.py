from django.shortcuts import render
from django.views import View
from users.models import ClientUser, DeliveryUser, SupermarketUser, SeparaterUser, Address
from auth_app.models import User

class Usuarios(View):
    def get(self, request):

        breadcrumbs = [
            {'name': 'Usuários'},
        ]

        editUsuarios = {
            'wire': "edit",
            'action': '#',
            'method': 'post',
            'id': 'editUsuarios',
            'title': 'Editar Usuário',
        }
     
        createUsuarios = {
            'wire': False,
            'action': '#',
            'method': 'post',
            'id': 'createUsuarios',
            'title': 'Criar Usuário',
        }

        # Aggregate all user types for admin table
        users = []
        for model, user_type in [
            (ClientUser, 'Cliente'),
            (DeliveryUser, 'Entregador'),
            (SupermarketUser, 'Supermercado'),
            (SeparaterUser, 'Separador'),
        ]:
            for u in model.objects.select_related('user').all():
                users.append({
                    'id': u.user.id,
                    'email': u.user.email,
                    'first_name': getattr(u, 'first_name', ''),
                    'last_name': getattr(u, 'last_name', ''),
                    'cpf': getattr(u, 'cpf', ''),
                    'type': user_type,
                })

        context = {
            'title': 'Traz Aí | Usuários',
            'breadcrumbs': breadcrumbs,
            'users': users,
            'editUsuarios': editUsuarios,
            'createUsuarios': createUsuarios,
        }

        return render(request, 'gerenciamento/usuarios.html', context)

class DadosMercado(View):
    def get(self, request):

        breadcrumbs = [
            {'name': 'Dados de Mercado'},
        ]

        context = {
            'title': 'Traz Aí | Dados de Mercado',
            'breadcrumbs': breadcrumbs,
        }

        return render(request, 'gerenciamento/dados_mercado.html', context)

class Enderecos(View):
    def get(self, request):

        breadcrumbs = [
            {'name': 'Endereços'},
        ]
        # Filtra endereços apenas do usuário atual
        enderecos = Address.objects.select_related('user').filter(user=request.user)

        editEnderecos = {
            'wire': "edit",
            'action': '#',
            'method': 'post',
            'id': 'editEnderecos',
            'title': 'Editar Endereço',
        }
    
        createEnderecos = {
            'wire': False,
            'action': '#',
            'method': 'post',
            'id': 'createEnderecos',
            'title': 'Criar Endereço',
        }

        context = {
            'title': 'Traz Aí | Endereços',
            'breadcrumbs': breadcrumbs,
            'enderecos': enderecos,
            'editEnderecos': editEnderecos,
            'createEnderecos': createEnderecos,
        }

        return render(request, 'gerenciamento/enderecos.html', context)

class Documentos(View):
    def get(self, request):

        breadcrumbs = [
            {'name': 'Documentos'},
        ]

        context = {
            'title': 'Traz Aí | Documentos',
            'breadcrumbs': breadcrumbs,
        }

        return render(request, 'gerenciamento/documentos.html', context)

class Servicos(View):
    def get(self, request):

        breadcrumbs = [
            {'name': 'Serviços'},
        ]

        context = {
            'title': 'Traz Aí | Serviços',
            'breadcrumbs': breadcrumbs,
        }

        return render(request, 'gerenciamento/servicos.html', context)
