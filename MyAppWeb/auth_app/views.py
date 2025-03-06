from django.shortcuts import render
from django.views import View
from auth_app.services import loginUser

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        return loginUser.login(request)

class Teste(View):
    def get(self, request):
        return render(request, 'teste/index.html')   