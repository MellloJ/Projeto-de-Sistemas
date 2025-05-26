from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Address, DeliveryUser, SeparaterUser

User = get_user_model()

class AddressSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(
        write_only=True,
        help_text="Email do usuário ao qual o endereço será associado."
    )
    city = serializers.CharField(help_text="Cidade do endereço.")
    state = serializers.CharField(help_text="Estado do endereço (ex.: SP, RJ).")
    street = serializers.CharField(help_text="Rua do endereço.")
    number = serializers.CharField(
        required=False,
        help_text="Número do endereço (opcional)."
    )
    quadra = serializers.CharField(
        required=False,
        help_text="Quadra do endereço (opcional)."
    )
    lote = serializers.CharField(
        required=False,
        help_text="Lote do endereço (opcional)."
    )
    reference = serializers.CharField(
        required=False,
        help_text="Ponto de referência do endereço (opcional)."
    )
    observation = serializers.CharField(
        required=False,
        help_text="Observações adicionais sobre o endereço (opcional)."
    )

    class Meta:
        model = Address
        fields = ['user_email', 'city', 'state', 'street', 'number', 'quadra', 'lote', 'reference', 'observation']

    def create(self, validated_data):
        user_email = validated_data.pop('user_email')
        try:
            user = User.objects.get(email=user_email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"user_email": "Usuário com este email não existe."})

        address = Address.objects.create(user=user, **validated_data)
        return address

    def validate(self, data):
        if 'content_type' in data or 'object_id' in data:
            raise serializers.ValidationError("Os campos content_type e object_id não devem ser fornecidos.")
        return data

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(help_text="Email do usuário.")
    password = serializers.CharField(
        write_only=True,
        help_text="Senha do usuário (mínimo 8 caracteres)."
    )

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class DeliveryUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(help_text="Dados do usuário associado ao entregador.")
    address = AddressSerializer(
        required=False,
        help_text="Endereço do entregador (opcional)."
    )
    first_name = serializers.CharField(help_text="Primeiro nome do entregador.")
    last_name = serializers.CharField(
        required=False,
        help_text="Sobrenome do entregador (opcional)."
    )
    cpf = serializers.CharField(help_text="CPF do entregador (11 dígitos, único).")

    class Meta:
        model = DeliveryUser
        fields = ['user', 'first_name', 'last_name', 'cpf', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        address_data = validated_data.pop('address', None)
        
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        delivery_user = DeliveryUser.objects.create(user=user, **validated_data)

        if address_data:
            Address.objects.create(user=user, **address_data)

        return delivery_user

class SeparaterUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(help_text="Dados do usuário associado ao separador.")
    address = AddressSerializer(
        required=False,
        help_text="Endereço do separador (opcional)."
    )
    first_name = serializers.CharField(help_text="Primeiro nome do separador.")
    last_name = serializers.CharField(
        required=False,
        help_text="Sobrenome do separador (opcional)."
    )
    cpf = serializers.CharField(help_text="CPF do separador (11 dígitos, único).")

    class Meta:
        model = SeparaterUser
        fields = ['user', 'first_name', 'last_name', 'cpf', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        address_data = validated_data.pop('address', None)
        
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        separater_user = SeparaterUser.objects.create(user=user, **validated_data)

        if address_data:
            Address.objects.create(user=user, **address_data)

        return separater_user