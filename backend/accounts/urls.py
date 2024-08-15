from django.urls import path
from .views import UserViewSet

urlpatterns = [
  path('', UserViewSet.as_view({'get': 'list'}), name='users'),
  path('/<int:pk>', UserViewSet.as_view({'get': 'retrieve'}, name='user-details')),
]