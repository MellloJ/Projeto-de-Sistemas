from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from auth_app import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Documentação das APIs do projeto",
        default_version="v1",
        description="Documentação da API da aplicação WEB (Django)",
        contact=openapi.Contact(email="jonatas.madeira@mail.uft.edu.br"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('confirm/', views.ConfirmEmail.as_view(), name='confirm_email'),
    path('create/market/', views.CreateMarket.as_view(), name='register_market'),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/signup/', views.UserClientView.as_view(), name='register_client_api'),

    path('api/create/market/', views.SupermarketView.as_view(), name='register_market_api'),

    # Swagger UI
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    
    # Redoc UI
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    
    # OpenAPI JSON/YAML
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]