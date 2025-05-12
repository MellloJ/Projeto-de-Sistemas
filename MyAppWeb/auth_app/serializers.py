from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User, Supermarket # as Client

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email  # Adicionando dados ao token
        return token

class UserClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'cpf', 'phone')
    
    def validate_cpf(self, value):
        from auth_app.services.validateUser import validate_cpf
        return validate_cpf(self, value)

    def create(self, validated_data):
        from auth_app.services.signupUser import signupClient
        return signupClient.register(**validated_data)

class MarketSeriallizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Supermarket
        fields = ('name', 'cnpj', 'phone', 'email', 'password')
    
    def create(self, validated_data):
        from auth_app.services.signupUser import signupMarket
        return signupMarket.register(**validated_data)