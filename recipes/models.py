from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    # picture = models.ImageField(upload_to='images', null=True, blank=True)
    instructions = models.TextField()
    public = models.BooleanField(default=False)
    saved = models.ManyToManyField(User, blank=True, related_name='recipe_saved')
    owner = models.ForeignKey(User, related_name='recipes')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipe_ingredients')

    def __str__(self):
        return self.title


class Menu(models.Model):
    name = models.CharField(max_length=200)
    public = models.BooleanField(default=False)
    saved = models.ManyToManyField(User, blank=True, related_name='menu_saved')
    owner = models.ForeignKey(User)
    recipes = models.ManyToManyField(Recipe, blank=True, related_name='menu_recipes')
    
    def __str__(self):
        return self.menu_name


class Grocery(models.Model):
    ingredients = models.ManyToManyField(Ingredient)
