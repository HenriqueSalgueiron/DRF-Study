from django.contrib.auth.models import User
from rest_framework import serializers

from .models import STATUS_CHOICES, Recipe


class RecipeSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  owner = serializers.ReadOnlyField(source='owner.id')
  title = serializers.CharField(max_length=100)
  description = serializers.CharField(required=False)
  directions = serializers.CharField()
  status = serializers.ChoiceField(required=False, choices=STATUS_CHOICES, default='draft')
  # picture = serializers.ImageField()

  def create(self, validated_data):
    return Recipe.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.directions = validated_data.get('directions', instance.directions)
    instance.status = validated_data.get('status', instance.status)
    # instance.picture = validated_data.get('picture', instance.picture)
    instance.save()
    return instance