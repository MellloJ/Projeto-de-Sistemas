from rest_framework import serializers
from users.models import SupermarketUser as Supermarket
from auth_app.models import User
from django.utils.timezone import now

class MarketSeriallizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    phone = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True)
    fantasy_name = serializers.CharField(read_only=True)

    class Meta:
        model = Supermarket
        fields = ('fantasy_name', 'cnpj', 'password', 'email', 'phone', 'name')
        extra_kwargs = {
            'fantasy_name': {'read_only': True},
        }

    def create(self, validated_data):
        # Cria o usuário base
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            user_type='supermarket',
            phone=validated_data['phone']
        )
        # Cria o perfil SupermarketUser
        market = Supermarket.objects.create(
            user=user,
            fantasy_name=validated_data['name'],
            cnpj=validated_data['cnpj']
        )
        return market, 'Usuário criado com sucesso, confirme seu email'