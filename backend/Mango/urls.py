from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from accounts import views

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls)
]
