from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Traz Aí API's",
        default_version="v1",
        description="Documentação das API's para gerenciamento de pedidos, usuários, produtos, e autenticação.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="suporte@exemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('core.urls')),
    path('', include('users.urls')),
    path('', include('auth_app.urls')),
    path('', include('market.urls')),
    path('admin/', admin.site.urls),
    path('pedidos/', include('pedidos.urls')),
    path('produtos/', include('produtos.urls')),
    path('unicorn', include('django_unicorn.urls')),
    path('gerenciamento/', include('gerenciamento.urls')),

    # Documentação Swagger e ReDoc
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
