from django_dump_die.middleware import dd
from users.services import googleLogin
from django.shortcuts import render
from django.views import View

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "login/login.html")