from recipes.models import Recipe
from recipes.serializers import RecipeSerializer 
from recipes.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions

## V3: Using generic class-based views
class RecipeView(generics.ListCreateAPIView): 
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class RecipeDetailsView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

## Other versions: 

# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import mixins

## V1: Explicitly defining the methods ##

# class RecipeView(APIView):
#   def get(self, request, format=None):
#     recipes = Recipe.objects.all()
#     serializer = RecipeSerializer(recipes, many=True)
#     return Response(serializer.data)

#   def post(sel, request, format=None):
#     serializer = RecipeSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RecipeDetailsView(APIView):
#   def get_object(self, pk):
#     try:
#       return Recipe.objects.get(pk=pk)
#     except Recipe.DoesNotExist:
#       raise Http404

#   def get(self, request, pk, format=None):
#     recipe = self.get_object(pk)
#     serializer = RecipeSerializer(recipe)
#     return Response(serializer.data)
  
#   def put(self, request, pk, format=None):
#     recipe = self.get_object(pk)
#     serializer = RecipeSerializer(recipe, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   def delete(self, request, pk, format=None):
#     recipe = self.get_object(pk)
#     recipe.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

## V2: Using mixins ##

# class RecipeView(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#   queryset = Recipe.objects.all()
#   serializer_class = RecipeSerializer

#   def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)
  
#   def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)

# class RecipeDetailsView(mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         generics.GenericAPIView):
#   queryset = Recipe.objects.all()
#   serializer_class = RecipeSerializer

#   def get(self, request, *args, **kwargs):
#     return self.retrieve(request, *args, **kwargs)
  
#   def put(self, request, *args, **kwargs):
#     return self.update(request, *args, **kwargs)
  
#   def delete(self, request, *args, **kwargs):
#     return self.destroy(request, *args, **kwargs)
