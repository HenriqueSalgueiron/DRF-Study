from django.urls import path
from recipes import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('', views.RecipeView.as_view(), name='recipes'),
  path('/<int:pk>', views.RecipeDetailsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns) # Com isso, o cliente pode especificar o formato da resposta na URL (.json, .xml, etc)

