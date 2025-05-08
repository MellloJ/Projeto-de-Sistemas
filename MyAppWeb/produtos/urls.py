from django.urls import path
from produtos import views


urlpatterns = [
    path('', views.Index.as_view(), name='produtos'),
    path('imagens/<str:arquivo>', views.Imagens.as_view(), name='imagens'),
]