from django.contrib import admin
from django.urls import include, path
from .views import api_root

urlpatterns = [
    path('', api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('recipes', include('recipes.urls')),
    path('users', include('accounts.urls'))
]
