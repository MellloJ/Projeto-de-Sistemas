from django.shortcuts import render, redirect
from django.views import View
from auth_app.services.loginUser import loginUser
from django.urls import reverse
from django.contrib.auth import logout

# Create your views here.

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
                return redirect(reverse('/'))
            else:
                return redirect(reverse('login'), {'errors': 'Não foi posivel realizar o login'})

class Logout(View):
    def logout(request):
        logout(request)
        return redirect(reverse('login'))