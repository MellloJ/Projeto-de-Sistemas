from django.urls import path
from .views import *

urlpatterns = [
    path('users/delivery-users/', DeliveryUserCreateView.as_view(), name='delivery-user-create'),
    path('users/separater-users/', SeparaterUserCreateView.as_view(), name='separater-user-create'),
    path('users/separater-users/delete/<int:pk>', SeparaterUserDeleteView.as_view(), name='separater-user-delete'),
    path('users/separater-users/edit/<int:pk>', SeparaterUserEditView.as_view(), name='separater-user-edit'),
    path('users/separater-users/get/all', SeparaterUserListView.as_view(), name='separater-user-get-all'),
    path('users/separater-users/get/<int:pk>', SeparaterUserGetView.as_view(), name='separater-user-get-one'),

    path('users/addresses/', AddressCreateView.as_view(), name='address-create'),
    path('users/addresses/delete/<int:pk>', AddressDeleteView.as_view(), name='address-delete'),
    path('users/addresses/edit/<int:pk>', AddressEditView.as_view(), name='address-edit'),
    path('users/addresses/get/all', AddressListView.as_view(), name='address-get-all'),
    path('users/addresses/get/<int:pk>', AddressGetView.as_view(), name='address-get-one'),

    path('users/clients/', ClientUserCreateView.as_view(), name='client-create'),
    path('users/clients/get/<int:pk>', ClientUserGetView.as_view(), name='client-get-one'),
]