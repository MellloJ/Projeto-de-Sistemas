from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Address, DeliveryUser, SeparaterUser, ClientUser, SupermarketUser
from rest_framework.exceptions import NotAuthenticated

User = get_user_model()

class AddressSerializer(serializers.ModelSerializer):
    zip_code = serializers.CharField(required=False, allow_null=True, help_text="CEP do endereço (opcional).")
    street = serializers.CharField(help_text="Logradouro (rua, avenida, etc.) do endereço.")
    number = serializers.CharField(required=False, allow_null=True, help_text="Número do endereço (opcional).")
    complement = serializers.CharField(required=False, allow_null=True, help_text="Complemento do endereço (opcional).")
    neighborhood = serializers.CharField(required=False, allow_null=True, help_text="Bairro do endereço (opcional).")
    city = serializers.CharField(help_text="Cidade do endereço.")
    state = serializers.CharField(help_text="Estado do endereço (ex.: SP, RJ).")

    class Meta:
        model = Address
        fields = ['user', 'zip_code', 'street', 'number', 'complement', 'neighborhood', 'city', 'state']

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

class ClientUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True, required=False)
    user_type = serializers.CharField(write_only=True, required=False)
    photo = serializers.CharField(write_only=True, required=False)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True, required=False)
    cpf = serializers.CharField(write_only=True)

    class Meta:
        model = ClientUser
        fields = ('email', 'password', 'phone', 'user_type', 'photo', 'first_name', 'last_name', 'cpf')

    def create(self, validated_data):
        from auth_app.services.signupUser import signupClient
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        phone = validated_data.pop('phone', None)
        user_type = validated_data.pop('user_type', 'client')
        photo = validated_data.pop('photo', None)
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name', '')
        cpf = validated_data.pop('cpf')
        user, message = signupClient.register(
            email=email,
            password=password,
            cpf=cpf,
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )
        if not user:
            raise serializers.ValidationError({'user': message})
        client_user = ClientUser.objects.create(user=user, first_name=first_name, last_name=last_name, cpf=cpf)
        return client_user

class SupermarketUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', required=False)
    phone = serializers.CharField(source='user.phone', required=False)
    fantasy_name = serializers.CharField(required=False)
    cnpj = serializers.CharField(required=False)

    class Meta:
        model = SupermarketUser
        fields = ('id', 'fantasy_name', 'cnpj', 'email', 'phone')

    def create(self, validated_data):
        # Espera dados aninhados de usuário
        user_data = validated_data.pop('user', None)
        if not user_data:
            raise serializers.ValidationError({'user': 'Dados do usuário são obrigatórios para cadastro.'})
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        instance = SupermarketUser.objects.create(user=user, **validated_data)
        return instance

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        # Atualiza campos do SupermarketUser
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        # Atualiza campos do usuário relacionado
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()
        instance.save()
        return instance

class UserProfileSerializer(serializers.Serializer):
    user = UserSerializer()
    profile_type = serializers.SerializerMethodField()
    profile_data = serializers.SerializerMethodField()

    def get_profile_type(self, obj):
        if isinstance(obj, ClientUser):
            return 'client'
        elif isinstance(obj, DeliveryUser):
            return 'delivery'
        elif isinstance(obj, SupermarketUser):
            return 'supermarket'
        elif isinstance(obj, SeparaterUser):
            return 'separater'
        return 'unknown'

    def get_profile_data(self, obj):
        if isinstance(obj, ClientUser):
            return {
                'first_name': obj.first_name,
                'last_name': obj.last_name,
                'cpf': obj.cpf
            }
        elif isinstance(obj, DeliveryUser):
            return {
                'first_name': obj.first_name,
                'last_name': obj.last_name,
                'cpf': obj.cpf
            }
        elif isinstance(obj, SupermarketUser):
            return {
                'fantasy_name': obj.fantasy_name,
                'cnpj': obj.cnpj
            }
        elif isinstance(obj, SeparaterUser):
            return {
                'first_name': obj.first_name,
                'last_name': obj.last_name,
                'cpf': obj.cpf
            }
        return {}