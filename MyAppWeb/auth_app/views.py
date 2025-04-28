from django.shortcuts import render, redirect
from django.views import View
from auth_app.services.loginUser import loginUser
from django.urls import reverse
from django.contrib.auth import logout
from auth_app.models import User

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken

# Create your views here.

class Register(View):
    def get(self, request):
        email = "teste@email.com"
        password = "123456"
        nomeCompleto = "Teste da Silva"

        user = User(email=email, password=password, nomeCompleto=nomeCompleto)
        user.set_password(password)
        user.save()

        return redirect(reverse('login'))

class Login(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        user = loginUser.auth(request, email, password, remember)

        if user is not None:
            login = loginUser.login(request, user)
            
            if login != False:

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                response = redirect(reverse('index'))

                response.set_cookie(
                    key="access_token",
                    value=access_token,
                    httponly=True,
                    secure=True,
                    samesite="Lax",
                    max_age=3600
                )

                response.set_cookie(
                    key="refresh_token",
                    value=str(refresh),
                    httponly=True,
                    secure=True,
                    samesite="Lax",
                    max_age=7 * 24 * 3600
                )

                return response
            else:
                context = {
                    'errors': 'Usuário ou senha incorretos'
                 }
                
            return render(request, 'login/index.html', context)

class Logout(View):
     def post(self, request):
        try:
            tokens = OutstandingToken.objects.filter(user=request.user)
            for token in tokens:
                BlacklistedToken.objects.get_or_create(token=token)
        except Exception as e:
            print(f"Erro ao invalidar tokens: {e}")

        response = redirect('index')
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        logout(request)

        return response

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer