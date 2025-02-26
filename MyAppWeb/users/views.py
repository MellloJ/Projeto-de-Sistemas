from django.shortcuts import render
from django.views import View
from users.services import googleLogin

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "login/login.html")