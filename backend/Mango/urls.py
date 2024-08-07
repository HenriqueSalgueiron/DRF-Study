from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.reverse import reverse
from .views import api_root

router = routers.DefaultRouter()

urlpatterns = [
    path('', api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('recipes', include('recipes.urls')),
    path('users', include('accounts.urls'))
]
