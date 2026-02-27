# from typing import __all__
from rest_framework import serializers
from .models import Food, User


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["id", "name", "taste", "region", "region", "main_ingredients", "optional_ingredients", "recipe", "calories", "prep_time", "optional_ingredients"]
      


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "first_name", "last_name"]