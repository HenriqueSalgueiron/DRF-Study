from django.db import models

STATUS_CHOICES = [
  ('active', 'Active'),
  ('inactive', 'Inactive'),
  ('draft', 'Draft'),
]

UNIT_CHOICES = [
  ('g', 'g'), # gramas
  ('kg', 'kg'), # kilogramas
  ('ml', 'ml'), # mililitros
  ('l', 'l'), # litros
  ('oz', 'oz'), # onças
  ('lb', 'lb'), # libras
  ('tsp', 'tsp'), # colher de chá
  ('tbsp', 'tbsp'), # colher de sopa
  ('cup', 'cup'), # xícara
  ('unit', 'unit'), # unidade
]

class Recipe(models.Model):
  owner = models.ForeignKey('auth.User', related_name='recipes', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=500, blank=True,null=True)
  directions = models.TextField()
  status = models.CharField(max_length=10, default='draft', choices=STATUS_CHOICES)
  deleted_at = models.DateTimeField(blank=True, null=True, editable=False)
  # picture = models.imageField(upload_to='recipes/images', blank=True, null=True)

  def __str__(self):
    return f"id: {self.id}, created: {self.created}, title: {self.title}, description: {self.description}, directions: {self.directions}, status: {self.status}, deleted_at: {self.deleted_at}"


class Ingredient(models.Model):
  name = models.CharField(max_length=100)
  recipes = models.ManyToManyField(Recipe, related_name='ingredients')

class RecipeIngredient(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  quantity = models.FloatField()
  unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
