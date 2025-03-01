from django.shortcuts import render
from django.views import View
from users.services import googleLogin
from 

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "login/login.html")


class Signup(View):
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

    return render(request, "name.html", {"form": form})
