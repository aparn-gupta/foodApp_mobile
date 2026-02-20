# from typing import __all__
from rest_framework import serializers
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["id", "name", "taste", "region", "region", "main_ingredients", "optional_ingredients", "recipe", "calories", "prep_time", "optional_ingredients"]
      