from django_dump_die.middleware import dd
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

