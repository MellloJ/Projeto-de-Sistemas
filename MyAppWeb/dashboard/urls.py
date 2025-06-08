from django.urls import path, include
from dashboard.views import *


urlpatterns = [
    path('', Index.as_view(), name='dashboard'),
]