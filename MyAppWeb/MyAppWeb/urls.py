from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('', include('users.urls')),
    path('', include('auth_app.urls')),
    path('produtos/', include('produtos.urls')),
    path('admin/', admin.site.urls),
]
