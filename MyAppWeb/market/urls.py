from django.urls import path
from market import views

urlpatterns = [
    path('market/create/', views.CreateMarket.as_view(), name='register_market'),
    path('api/market/create/', views.SupermarketView.as_view(), name='register_market_api'),
    path('api/create/market', views.SupermarketView.as_view(), name='api-create-market'),
]