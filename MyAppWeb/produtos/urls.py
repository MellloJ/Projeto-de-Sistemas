from django.urls import path
from produtos import views


urlpatterns = [
    path('', views.Index.as_view(), name='index')
]