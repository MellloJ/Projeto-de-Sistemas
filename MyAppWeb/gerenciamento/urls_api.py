from django.urls import path
from .views_api import AddressListCreateView, AddressRetrieveUpdateDestroyView, CepLookupAPIView

urlpatterns = [
    path("enderecos/", AddressListCreateView.as_view(), name="endereco-list-create"),
    path("enderecos/<int:pk>/", AddressRetrieveUpdateDestroyView.as_view(), name="endereco-detail"),
    path("cep/<str:cep>/", CepLookupAPIView.as_view(), name="cep-lookup"),
]
