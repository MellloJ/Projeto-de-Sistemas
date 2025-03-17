from django_dump_die.middleware import dd
from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, "index.html")