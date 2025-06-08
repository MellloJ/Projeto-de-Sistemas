from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User # as Client
from auth_app.services.validateUser import validate_cpf
from django.utils.timezone import now

# Removed redundant local definition of validate_cpf

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email  # Adicionando dados ao token
        return token

class UserClientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    cpf = serializers.CharField(write_only=True, required=True, validators=[validate_cpf])
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'user_type', 'is_active', 'is_staff', 'last_login', 'date_joined', 'first_name', 'last_name', 'cpf', 'password']
        extra_kwargs = {
            'user_type': {'default': 'client'},
            'is_active': {'default': False},
            'is_staff': {'default': False},
            'last_login': {'required': False},
            'date_joined': {'required': False},
        }

    def create(self, validated_data):
        validated_data['last_login'] = now()
        validated_data['date_joined'] = now()
        # Remove fields not in User
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        cpf = validated_data.pop('cpf')
        password = validated_data.pop('password')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=password,
            groupName='client',
            phone=validated_data.get('phone'),
            last_login=validated_data['last_login'],
            date_joined=validated_data['date_joined']
        )
        # Cria o perfil ClientUser
        from users.models import ClientUser
        ClientUser.objects.create(user=user, first_name=first_name, last_name=last_name, cpf=cpf)
        return user, 'Usuário criado com sucesso, confirme seu email'