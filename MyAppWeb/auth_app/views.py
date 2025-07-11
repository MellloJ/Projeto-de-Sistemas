from django.shortcuts import render, redirect
from django.views import View
from auth_app.services.loginUser import loginUser
from django.urls import reverse
from django.contrib.auth import logout
from auth_app.services.signupUser import signupClient
from .forms import signupUserForm
from auth_app.services.confirmEmailUser import sendMail
from auth_app.models import User
from users.models import ClientUser
from core.consts import CATEGORIAS_ALIMENTOS

# Importando jwt do rest
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken

class Signup(View):
    def get(self, request):
         return render(request, 'signup/signup.html', {'form': signupUserForm()})
    
    def post(self, request):
        form = signupUserForm(request.POST)
        if form.is_valid():
            user, message = signupClient.register(
                email=form.cleaned_data['email'],
                password=request.POST.get('password'),
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                cpf=form.cleaned_data['cpf'],
                user_type='client',
                phone=form.cleaned_data['phone'],
            )
            if user is None:
                context = {
                    'form': form,
                    'errors': message,
                }
                return render(request, 'signup/signup.html', context)
            else:
                sendMail(request, user)
                context = {
                    'title': 'Traz Aí | Home',
                    'categories': CATEGORIAS_ALIMENTOS,
                }
                return render(request, "index.html",context)
                # return render(request, 'signup/confirm.html', {'email': user.email, 'completeName': user.completeName})
        else:
            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'signup/signup.html', context)

class ConfirmEmail(View):
    def get(self, request):
        token = request.GET.get('token')
        if token:
            try:
                token= AccessToken(token)
                user_id = token['user_id']
                purpose = token['purpose']
                if purpose != 'email_confirmation':
                    return render(request, 'signup/confirmFail.html', {'error': 'Token inválido ou expirado'})
                
                user = User.objects.get(id=user_id)
                user.is_active = True
                user.save()

            except Exception as e:
                print(f"Erro ao confirmar o email: {e}")
                return render(request, 'signup/confirmFail.html', {'error': 'Token inválido ou expirado'})
        else:
            return render(request, 'signup/confirmFail.html', {'error': 'Token não fornecido'})
        return render(request, 'signup/confirmed.html')

class Login(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        user = loginUser.auth(request, email, password, remember)

        if user is not None:
            if user.is_active == False:
                context = {
                    'errors': 'Email do usuário não confirmado'
                }
                return render(request, 'login/index.html', context)

            login = loginUser.do_login(request, user)
            
            if login != False:

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                response = redirect(reverse('home'))

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

        context = {
            'errors': 'Usuário ou senha incorretos'
            }
                
        return render(request, 'login/index.html', context)
            
class Logout(View):
     def get(self, request):
        try:
            tokens = OutstandingToken.objects.filter(user=request.user)
            for token in tokens:
                BlacklistedToken.objects.get_or_create(token=token)
        except Exception as e:
            print(f"Erro ao invalidar tokens: {e}")

        response = redirect('home')
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        logout(request)

        return response

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer