from django.db import models
from django.contrib.auth.models import User


# class Menu(models.Model):
    # menu_name = models.CharField(max_length=200)
    # public = models.BooleanField(default=False)
    # saved = models.ManyToManyField(User, blank=True, related_name='menu_saved')
    # owner = models.ForeignKey(User)
    
    # def __str__(self):
        # return self.menu_name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)


class Recipe(models.Model):
    # menus = models.ManyToManyField(Menu, blank=True)
    title = models.CharField(max_length=200)
    # picture = models.ImageField(upload_to='images', null=True, blank=True)
    instructions = models.TextField()
    public = models.BooleanField(default=False)
    saved = models.ManyToManyField(User, blank=True, related_name='recipe_saved')
    owner = models.ForeignKey(User, related_name='recipes')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipe_ingredients')

    def __str__(self):
        return self.title


# class GroceryList(models.Model):
    # ingredients = models.ManyToManyField(Ingredient)
