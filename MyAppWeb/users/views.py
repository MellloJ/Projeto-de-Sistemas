from django.shortcuts import render
from django.views import View
from users.services import googleLogin
from .signupValidation import signupForm

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "login/login.html")


class Signup(View):
    form = signupForm()
    def get(self, request):
        return render(request, "signup/signup.html", {'form': form})

    def post(request):
        form = signupForm(request.POST)
        # if this is a POST request we need to process the form data
        if form.is_valid():

            return HttpResponseRedirect("/thanks/")
