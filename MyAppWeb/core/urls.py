from django.urls import path
from core import views


urlpatterns = [
    path('home/', views.Index.as_view(), name='home')
]