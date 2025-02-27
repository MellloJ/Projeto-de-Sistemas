from django.urls import path
from auth import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('teste/', views.Teste.as_view(), name='teste'),
]