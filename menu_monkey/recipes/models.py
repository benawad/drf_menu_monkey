from django.db import models
from django.contrib.auth.models import User

# class Menu(models.Model):
    # group_name = models.CharField(max_length=200)
    # public = models.BooleanField(default=False)
    # saved = models.ManyToManyField(User, blank=True, related_name='menu_saved')
    # owner = models.ForeignKey(User)
    
    # def __str__(self):
        # return self.group_name

class Recipe(models.Model):
    # menus = models.ManyToManyField(Menu, blank=True)
    title = models.CharField(max_length=200)
    # picture = models.ImageField(upload_to='images', null=True, blank=True)
    instructions = models.TextField()
    public = models.BooleanField(default=False)
    saved = models.ManyToManyField(User, blank=True, related_name='recipe_saved')
    owner = models.ForeignKey(User, related_name='recipes')

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients')
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=1)

    def __unicode__(self):
        return '%d: %s' % (self.amount, self.name)

# class GroceryList(models.Model):
    # ingredients = models.ManyToManyField(Ingredient)
