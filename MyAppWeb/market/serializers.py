from rest_framework import serializers
from .models import Supermarket

class MarketSeriallizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Supermarket
        fields = ('name', 'cnpj', 'phone', 'email', 'password')
    
    def create(self, validated_data):
        from market.services.signupMarket import signupMarket
        return signupMarket.register(**validated_data)