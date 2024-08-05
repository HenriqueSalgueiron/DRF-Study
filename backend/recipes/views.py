from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def recipe_view(request):
  if request.method == 'GET':
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True) # translates Native into Python
    return JsonResponse(serializer.data, safe=False) # translates Python into JSON
  elif request.method == 'POST':
    data = JSONParser().parse(request) # parses and translates JSON into Python
    serializer = RecipeSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def recipe_details_view(request, pk):
  try:
    recipe = Recipe.objects.get(pk=pk)
  except Recipe.DoesNotExist:
    return HttpResponse(status=404)
  
  if request.method == 'GET':
    serializer = RecipeSerializer(recipe)
    return JsonResponse(serializer.data)
  
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = RecipeSerializer(recipe, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
  
  elif request.method == 'DELETE':
    recipe.delete()
    return HttpResponse(status=204)