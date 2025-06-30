from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Address, DeliveryUser, SeparaterUser, ClientUser
from .serializers import AddressSerializer, DeliveryUserSerializer, SeparaterUserSerializer, ClientUserSerializer

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
                        'number': openapi.Schema(type=openapi.TYPE_STRING, description="Número do endereço (opcional)")
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
                    "number": "123"
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
                        'number': openapi.Schema(type=openapi.TYPE_STRING, description="Número do endereço (opcional)")
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
                    "number": "456"
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
                'city': openapi.Schema(type=openapi.TYPE_STRING, description="Cidade do endereço"),
                'state': openapi.Schema(type=openapi.TYPE_STRING, description="Estado do endereço (ex.: MG)"),
                'street': openapi.Schema(type=openapi.TYPE_STRING, description="Rua do endereço"),
                'number': openapi.Schema(type=openapi.TYPE_STRING, description="Número do endereço (opcional)"),
                'complement': openapi.Schema(type=openapi.TYPE_STRING, description="Complemento do endereço (opcional)"),
                'neighborhood': openapi.Schema(type=openapi.TYPE_STRING, description="Bairro do endereço (opcional)"),
                'zip_code': openapi.Schema(type=openapi.TYPE_STRING, description="CEP do endereço (opcional)")
            },
            required=['city', 'state', 'street'],
            example={
                "city": "Belo Horizonte",
                "state": "MG",
                "street": "Rua dos Ipês",
                "number": "789",
                "zip_code": "12345-678",
                "complement": "Apto 101",
                "neighborhood": "Centro"
            }
        ),
        responses={
            201: AddressSerializer,
            400: openapi.Response("Erro nos dados fornecidos, como usuário inválido ou campos obrigatórios ausentes.")
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
                'city': openapi.Schema(type=openapi.TYPE_STRING, description="Cidade do endereço"),
                'state': openapi.Schema(type=openapi.TYPE_STRING, description="Estado do endereço (ex.: MG)"),
                'street': openapi.Schema(type=openapi.TYPE_STRING, description="Rua do endereço"),
                'number': openapi.Schema(type=openapi.TYPE_STRING, description="Número do endereço (opcional)"),
                'zip_code': openapi.Schema(type=openapi.TYPE_STRING, description="CEP do endereço (opcional)"),
                'complement': openapi.Schema(type=openapi.TYPE_STRING, description="Complemento do endereço (opcional)"),
                'neighborhood': openapi.Schema(type=openapi.TYPE_STRING, description="Bairro do endereço (opcional)"),
            },
            required=['city', 'state', 'street'],
            example={
                "user_email" : "admin@example.com",
                "city" : "Extrema",
                "state" : "MG",
                "street" : "Av. das Palmeiras",
                "number" : "123",
                "zip_code": "12345-678",
                "complement": "Apto 101",
                "neighborhood": "Centro"
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
                'zip_code': openapi.Schema(type=openapi.TYPE_STRING, description="CEP do endereço (opcional)"),
                'complement': openapi.Schema(type=openapi.TYPE_STRING, description="Complemento do endereço (opcional)"),
                'neighborhood': openapi.Schema(type=openapi.TYPE_STRING, description="Bairro do endereço (opcional)"),
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


class AddressListUserView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Address.objects.filter(user__id=user_id)

    @swagger_auto_schema(
        operation_description="Obtém todos os endereços associados a um usuário específico, identificado pelo email.",
        responses={
            200: AddressSerializer(many=True),
            404: openapi.Response("Usuário não encontrado ou sem endereços associados.")
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

class ClientUserGetView(generics.RetrieveAPIView):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserSerializer
    lookup_field = "pk"

    @swagger_auto_schema(
        operation_description="Retorna os dados do usuário autenticado.",
        responses={
            200: openapi.Response(
                description="Dados do usuário",
                schema=ClientUserSerializer
            ),
            401: openapi.Response(description="Não autenticado"),
            404: openapi.Response(description="Usuário não encontrado"),
        }
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ClientUserCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Cria um novo usuário do tipo ClientUser com informações fornecidas",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="Email do usuário (único)"),
                'password' : openapi.Schema(type=openapi.TYPE_STRING, description="Senha do usuário (mínimo 8 caracteres)"),
                'phone' : openapi.Schema(type=openapi.TYPE_STRING, description="Número de telefone do usuário (opcional)"),
                'first_name' : openapi.Schema(type=openapi.TYPE_STRING, description="Primeiro nome do usuário"),
                'last_name' : openapi.Schema(type=openapi.TYPE_STRING, description="Sobrenome do usuário (opcional)"),
                'cpf' : openapi.Schema(type=openapi.TYPE_STRING, description="CPF do usuário (11 dígitos, único)"),
            },
            required=['email', 'password', 'first_ name','cpf'],
            example={
                "user": {
                    "email": "joao@email.com",
                    "password": "123456789",
                    "phone": "31999999999"
                },
                "first_name": "João",
                "last_name": "Silva",
                "cpf": "34005834132",
            }
        ),
        responses={
            201: openapi.Response("Usuário criado com sucesso"),
            400: openapi.Response("Erro de validação nos dados enviados"),
        }
    )
    def post(self, request):
        serializer = ClientUserSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                clientUser = serializer.save()
            except Exception as e:
                return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            if clientUser:
                return Response({
                    'clientUser': {
                        'email': clientUser.user.email,
                        'first_name': clientUser.first_name,
                        'last_name': clientUser.last_name
                    }
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({'errors': message}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ClientUserDeleteView(generics.DestroyAPIView):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserSerializer
    lookup_field = 'user__email'

    @swagger_auto_schema(
        operation_description="Deleta um usuário do tipo ClientUser, identificado pelo email.",
        responses={
            204: openapi.Response("Usuário deletado com sucesso"),
            404: openapi.Response("Usuário não encontrado.")
        },
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class ClientUserEditView(generics.UpdateAPIView):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserSerializer
    lookup_field = 'user__email'

    @swagger_auto_schema(
        operation_description="Atualiza os dados de um cliente existente, identificado pelo usuário associado.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'email': openapi.Schema(type=openapi.TYPE_STRING, description="Email do cliente associado"),
                        'password': openapi.Schema(type=openapi.TYPE_STRING, description="Senha do cliente (mínimo 8 caracteres)")
                    }
                ),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description="Primeiro nome do cliente"),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description="Sobrenome do cliente (opcional)"),
                'cpf': openapi.Schema(type=openapi.TYPE_STRING, description="CPF do cliente (11 dígitos, único)")
            },
            required=['user', 'first_name', 'cpf'],
            example={
                "user": {
                    "email": "clientuser@example.com",
                    "password": "123456789"
                },
                "first_name": "João",
                "last_name": "Silva",
                "cpf": "59331091001"
            }
        ),
        responses={
            200: ClientUserSerializer,
            400: openapi.Response("Erro na atualização. Verifique os dados enviados."),
            404: openapi.Response("Usuário não encontrado.")
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Atualiza parcialmente os dados de um endereço existente, identificado pelo ID.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description="Primeiro nome do cliente"),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description="Sobrenome do cliente"),
                'cpf': openapi.Schema(type=openapi.TYPE_STRING, description="CPF do cliente (11 dígitos, único)")
            },
            example={
                "first_name": "Carlos",
                "last_name": "Oliveira"
            }
        ),
        responses={
            200: ClientUserSerializer,
            400: openapi.Response("Erro nos dados fornecidos."),
            404: openapi.Response("Usuário não encontrado.")
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class ClientUserListView(generics.ListAPIView):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserSerializer

    @swagger_auto_schema(
        operation_description="Lista todos os usuários cadastrados do tipo cliente (ClientUser).",
        responses={
            200: ClientUserSerializer(many=True),
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)