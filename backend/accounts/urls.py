from django.urls import path
from accounts import views

from . import views

urlpatterns = [
  path('', views.UserView.as_view(), name='users'),
  path('/<int:pk>', views.UserDetailsView.as_view())
]