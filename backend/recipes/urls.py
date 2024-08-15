from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import RecipeViewSet

recipe_list = RecipeViewSet.as_view({
  'get': 'list',
  'post': 'create'
})

recipe_details = RecipeViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'delete': 'destroy'
})

urlpatterns = [
  path('', recipe_list, name='recipes'),
  path('/<int:pk>', recipe_details, name='recipe-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns) # Com isso, o cliente pode especificar o formato da resposta na URL (.json, .xml, etc)

