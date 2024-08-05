from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer 
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
@csrf_exempt
def recipe_view(request):
  if request.method == 'GET':
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True) # translates Native into Python
    return Response(serializer.data)
  elif request.method == 'POST':
    data = JSONParser().parse(request) # parses and translates JSON into Python
    serializer = RecipeSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def recipe_details_view(request, pk):
  try:
    recipe = Recipe.objects.get(pk=pk)
  except Recipe.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = RecipeSerializer(recipe, data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)