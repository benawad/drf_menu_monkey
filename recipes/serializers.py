from rest_framework import serializers
from recipes.models import Recipe, Ingredient, Menu, Grocery
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu


class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'recipes')
