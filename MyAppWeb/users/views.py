from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Address, DeliveryUser, SeparaterUser
from .serializers import AddressSerializer, DeliveryUserSerializer, SeparaterUserSerializer

class DeliveryUserCreateView(generics.CreateAPIView):
    queryset = DeliveryUser.objects.all()
    serializer_class = DeliveryUserSerializer

    @swagger_auto_schema(
        operation_description="Cria um novo usuário do tipo DeliveryUser com informações pessoais e endereço opcional.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'email': openapi.Schema(type=openapi.TYPE_STRING, description="Email do usuário"),
                        'password': openapi.Schema(type=openapi.TYPE_STRING, description="Senha do usuário")
                    }
                ),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description="Primeiro nome do entregador"),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description="Sobrenome do entregador (opcional)"),
                'cpf': openapi.Schema(type=openapi.TYPE_STRING, description="CPF do entregador (11 dígitos, único)"),
                'address': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'city': openapi.Schema(type=openapi.TYPE_STRING, description="Cidade do endereço"),
                        'state': openapi.Schema(type=openapi.TYPE_STRING, description="Estado do endereço (ex.: SP)"),
                        'street': openapi.Schema(type=openapi.TYPE_STRING, description="Rua do endereço"),
                        'number': openapi.Schema(type=openapi.TYPE_STRING, description="Número do endereço (opcional)"),
                        'quadra': openapi.Schema(type=openapi.TYPE_STRING, description="Quadra do endereço (opcional)"),
                        'lote': openapi.Schema(type=openapi.TYPE_STRING, description="Lote do endereço (opcional)"),
                        'reference': openapi.Schema(type=openapi.TYPE_STRING, description="Ponto de referência (opcional)"),
                        'observation': openapi.Schema(type=openapi.TYPE_STRING, description="Observações (opcional)")
                    }
                )
            },
            required=['user', 'first_name', 'cpf'],
            example={
                "user": {
                    "email": "entregador1@example.com",
                    "password": "SenhaSegura123"
                },
                "first_name": "João",
                "last_name": "Silva",
                "cpf": "12345678901",
                "address": {
                    "city": "São Paulo",
                    "state": "SP",
                    "street": "Rua das Flores",
                    "number": "123",
                    "quadra": "Q1",
                    "lote": "L5",
                    "reference": "Próximo à praça",
                    "observation": "Casa com portão azul"
                }
            }
        ),
        responses={
            201: DeliveryUserSerializer,
            400: openapi.Response("Erro nos dados fornecidos, como CPF inválido ou email já existente.")
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SeparaterUserCreateView(generics.CreateAPIView):
    queryset = SeparaterUser.objects.all()
    serializer_class = SeparaterUserSerializer

    @swagger_auto_schema(
        operation_description="Cria um novo usuário do tipo SeparaterUser com informações pessoais e endereço opcional.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'email': openapi.Schema(type=openapi.TYPE_STRING, description="Email do usuário"),
                        'password': openapi.Schema(type=openapi.TYPE_STRING, description="Senha do usuário")
                    }
                ),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description="Primeiro nome do separador"),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description="Sobrenome do separador (opcional)"),
                'cpf': openapi.Schema(type=openapi.TYPE_STRING, description="CPF do separador (11 dígitos, único)"),
                'address': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'city': openapi.Schema(type=openapi.TYPE_STRING, description="Cidade do endereço"),
                        'state': openapi.Schema(type=openapi.TYPE_STRING, description="Estado do endereço (ex.: RJ)"),
                        'street': openapi.Schema(type=openapi.TYPE_STRING, description="Rua do endereço"),
                        'number': openapi.Schema(type=openapi.TYPE_STRING, description="Número do endereço (opcional)"),
                        'quadra': openapi.Schema(type=openapi.TYPE_STRING, description="Quadra do endereço (opcional)"),
                        'lote': openapi.Schema(type=openapi.TYPE_STRING, description="Lote do endereço (opcional)"),
                        'reference': openapi.Schema(type=openapi.TYPE_STRING, description="Ponto de referência (opcional)"),
                        'observation': openapi.Schema(type=openapi.TYPE_STRING, description="Observações (opcional)")
                    }
                )
            },
            required=['user', 'first_name', 'cpf'],
            example={
                "user": {
                    "email": "separador1@example.com",
                    "password": "SenhaSegura456"
                },
                "first_name": "Maria",
                "last_name": "Souza",
                "cpf": "98765432109",
                "address": {
                    "city": "Rio de Janeiro",
                    "state": "RJ",
                    "street": "Avenida Atlântica",
                    "number": "456",
                    "quadra": "Q2",
                    "lote": "L10",
                    "reference": "Perto do mercado",
                    "observation": "Apartamento 101"
                }
            }
        ),
        responses={
            201: SeparaterUserSerializer,
            400: openapi.Response("Erro nos dados fornecidos, como CPF inválido ou email já existente.")
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class AddressCreateView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @swagger_auto_schema(
        operation_description="Cria um novo endereço associado a um usuário existente, identificado pelo email.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user_email': openapi.Schema(type=openapi.TYPE_STRING, description="Email do usuário existente"),
                'city': openapi.Schema(type=openapi.TYPE_STRING, description="Cidade do endereço"),
                'state': openapi.Schema(type=openapi.TYPE_STRING, description="Estado do endereço (ex.: MG)"),
                'street': openapi.Schema(type=openapi.TYPE_STRING, description="Rua do endereço"),
                'number': openapi.Schema(type=openapi.TYPE_STRING, description="Número do endereço (opcional)"),
                'quadra': openapi.Schema(type=openapi.TYPE_STRING, description="Quadra do endereço (opcional)"),
                'lote': openapi.Schema(type=openapi.TYPE_STRING, description="Lote do endereço (opcional)"),
                'reference': openapi.Schema(type=openapi.TYPE_STRING, description="Ponto de referência (opcional)"),
                'observation': openapi.Schema(type=openapi.TYPE_STRING, description="Observações (opcional)")
            },
            required=['user_email', 'city', 'state', 'street'],
            example={
                "user_email": "entregador1@example.com",
                "city": "Belo Horizonte",
                "state": "MG",
                "street": "Rua dos Ipês",
                "number": "789",
                "quadra": "Q3",
                "lote": "L15",
                "reference": "Ao lado da escola",
                "observation": "Casa com jardim"
            }
        ),
        responses={
            201: AddressSerializer,
            400: openapi.Response("Erro nos dados fornecidos, como email inválido ou campos obrigatórios ausentes.")
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class AddressDeleteView(generics.DestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'pk'

    @swagger_auto_schema(
        operation_description="Deleta endereço existente, identificado pelo id.",
        responses={
            204: openapi.Response("Endereço deletado com sucesso"),
            404: openapi.Response("Id fornecido não existe no banco")
        },
    )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class AddressEditView(generics.UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'pk'

    @swagger_auto_schema(
        operation_description="Atualiza os dados de um endereço existente, identificado pelo ID.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user_email' : openapi.Schema(type=openapi.TYPE_STRING, description="Email do usuário associado ao endereço"),
                'city': openapi.Schema(type=openapi.TYPE_STRING, description="Cidade do endereço"),
                'state': openapi.Schema(type=openapi.TYPE_STRING, description="Estado do endereço (ex.: MG)"),
                'street': openapi.Schema(type=openapi.TYPE_STRING, description="Rua do endereço"),
                'number': openapi.Schema(type=openapi.TYPE_STRING, description="Número do endereço (opcional)"),
                'quadra': openapi.Schema(type=openapi.TYPE_STRING, description="Quadra do endereço (opcional)"),
                'lote': openapi.Schema(type=openapi.TYPE_STRING, description="Lote do endereço (opcional)"),
                'reference': openapi.Schema(type=openapi.TYPE_STRING, description="Ponto de referência (opcional)"),
                'observation': openapi.Schema(type=openapi.TYPE_STRING, description="Observações (opcional)")
            },
            required=['user_emal','city', 'state', 'street'],
            example={
                "user_email" : "admin@example.com",
                "city" : "Extrema",
                "state" : "MG",
                "street" : "Av. das Palmeiras",
                "number" : "123",
                "quadra" : "Q1",
                "lote" : "L10",
                "reference" : "Próximo ao mercado",
                "observation" : "Apartamento no 2º andar"
            }
        ),
        responses={
            200: AddressSerializer,
            400: openapi.Response("Erro na atualização. Verifique os dados enviados."),
            404: openapi.Response("Endereço não encontrado.")
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Atualiza parcialmente os dados de um endereço existente, identificado pelo ID.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'city': openapi.Schema(type=openapi.TYPE_STRING, description="Cidade do endereço"),
                'state': openapi.Schema(type=openapi.TYPE_STRING, description="Estado do endereço (ex.: MG)"),
                'street': openapi.Schema(type=openapi.TYPE_STRING, description="Rua do endereço"),
                'number': openapi.Schema(type=openapi.TYPE_STRING, description="Número do endereço (opcional)"),
                'quadra': openapi.Schema(type=openapi.TYPE_STRING, description="Quadra do endereço (opcional)"),
                'lote': openapi.Schema(type=openapi.TYPE_STRING, description="Lote do endereço (opcional)"),
                'reference': openapi.Schema(type=openapi.TYPE_STRING, description="Ponto de referência (opcional)"),
                'observation': openapi.Schema(type=openapi.TYPE_STRING, description="Observações (opcional)")
            },
            example={
                "street": "Rua Nova",
                "number": "456"
            }
        ),
        responses={
            200: AddressSerializer,
            400: openapi.Response("Erro nos dados fornecidos."),
            404: openapi.Response("Endereço não encontrado.")
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @swagger_auto_schema(
        operation_description="Lista todos os endereços cadastrados.",
        responses={
            200: AddressSerializer(many=True),
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AddressGetView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "pk"

    @swagger_auto_schema(
        operation_description="Obtém os detalhes de um endereço específico, identificado pelo ID.",
        responses={
            200: AddressSerializer,
            404: openapi.Response("Endereço não encontrado.")
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)