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
