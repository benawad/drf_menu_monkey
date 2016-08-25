from rest_framework import serializers
from recipes.models import Recipe, Ingredient
from django.contrib.auth.models import User


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.StringRelatedField(many=True)
    class Meta:
        model = Recipe


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'recipes')
