from django.urls import path
from .views import *

urlpatterns = [
    path('users/delivery-users/', DeliveryUserCreateView.as_view(), name='delivery-user-create'),
    path('users/separater-users/', SeparaterUserCreateView.as_view(), name='separater-user-create'),

    path('users/addresses/', AddressCreateView.as_view(), name='address-create'),
    path('users/addresses/delete/<int:pk>', AddressDeleteView.as_view(), name='address-delete'),
]