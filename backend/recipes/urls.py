from django.urls import path
from recipes import views

urlpatterns = [
  path('', views.recipe_view),
  path('/<int:pk>', views.recipe_details_view),
]

