from django.contrib.auth.models import User
from recipes.models import Recipe
from rest_framework import serializers 


class UserSerializer(serializers.ModelSerializer):
  recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())

  class Meta:
    model = User
    fields = ['id', 'username', 'recipes']