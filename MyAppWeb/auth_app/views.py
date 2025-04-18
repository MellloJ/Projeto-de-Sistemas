from django.shortcuts import render, redirect
from django.views import View
from auth_app.services.loginUser import loginUser
from django.urls import reverse
from django.contrib.auth import logout
from auth_app.models import User

# Importando jwt do rest
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken

from django.contrib.auth.models import Group, Permission
from django.utils.timezone import now

class Register(View):
    def get(self, request):
         return render(request, 'signup/signup.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpf = request.POST.get('cpf')
        phone = request.POST.get('phone')
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        completeName = (first_name, last_name)
        completeName = " ".join(completeName)

        is_superuser = False
        is_active = True
        is_staff = False
        date_joined = now()
        last_login = now()

        # Verifica se o usuário já existe
        if User.objects.filter(email=email).exists():
            context = {
                'errors': 'Email já cadastrado'
            }
            return render(request, 'login/index.html', context)

        user = User(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            completeName=completeName,
            cpf=cpf,
            phone=phone,
            is_superuser=is_superuser,
            is_active=is_active,
            is_staff=is_staff,
            date_joined=date_joined,
            last_login=last_login

        )

        user.set_password(password)
        user.save()

        return redirect(reverse('login'))

"""    class Signup(View):
        def get(self, request):
            return render(request, "signup/signup.html")

        def formHandler(request):
            # if this is a POST request we need to process the form data
            if request.method == "POST":
                # create a form instance and populate it with data from the request:
                form = NameForm(request.POST)
                # check whether it's valid:
                if form.is_valid():
                    # process the data in form.cleaned_data as required
                    # ...
                    # redirect to a new URL:
                    return HttpResponseRedirect("/thanks/")

            # if a GET (or any other method) we'll create a blank form
            else:
                form = NameForm()

            return render(request, "name.html", {"form": form}) """

class Login(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        user = loginUser.auth(request, email, password, remember)

        if user is not None:
            login = loginUser.do_login(request, user)
            
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