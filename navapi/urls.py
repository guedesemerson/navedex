from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Nav API",
        default_version='v1',
        description="Construído por Emerson Guedes de Oliveira",
        contact=openapi.Contact(email="guedes.emerson@hotmail.com"),
        license=openapi.License(name="Licença de teste"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('navers/', include('navers.urls')),
    path('users/', include('users.urls')),
    path('projects/', include('projetos.urls')),
    path('', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),

]
