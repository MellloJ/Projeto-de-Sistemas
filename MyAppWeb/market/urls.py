from django.urls import path
from market import views

urlpatterns = [
    path('market/create/', views.CreateMarket.as_view(), name='register_market'),
    path('api/market/create/', views.SupermarketView.as_view(), name='register_market_api'),
]