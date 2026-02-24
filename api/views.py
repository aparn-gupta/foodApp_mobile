from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer
from django.contrib.postgres.search import SearchQuery
from django.db.models import Func, F
from rest_framework.response import Response


class AllFood(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
# Create your views here.


class FoodDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = "id"



# class Options(generics.ListCreateAPIView):

def options(req):
    # queryset = Food.objects.all()
    requestedOption = req.GET.get("requested")

    ALLOWED_FIELDS = ["name", "taste", "calories", "prep_time", "recipe", "cooking_method", "ingredients", "region" ]

    if requestedOption not in ALLOWED_FIELDS:
        return JsonResponse({"error": "Invalid requested"}, status=400)

    if requestedOption != 'ingredients':

      queryset =   Food.objects.values_list(requestedOption, flat=True).distinct().order_by(requestedOption)

    else:

        queryset = (
            Food.objects
            .annotate(
                ingredient=Func(
                    F("main_ingredients"),
                    function="unnest"
                )
            )
            .values_list("ingredient", flat=True)
            .distinct()
        )


    return JsonResponse(list(queryset), safe=False)






def loadDishes(request):

    tastePreferences = request.GET.get("taste")

    regionPreferences = request.GET.get("region")
    caloriePreferences = request.GET.get("calories")


    cookingMethodPreferences = request.GET.get("cooking_method")
    prepTimePreferences = request.GET.get("prep_time")


    ingredientPreferences = request.GET.get("ingredients")

    filter = {}

    if tastePreferences:
        filter["taste"] = tastePreferences

    if regionPreferences:
        filter["region"] = regionPreferences

    if caloriePreferences:
        caloriePreferencesMin, caloriePreferencesMax = caloriePreferences.split("-")

        filter["calories__gte"] = int(caloriePreferencesMin)
        filter["calories__lte"] = int(caloriePreferencesMax)

    if prepTimePreferences:
        prepTimePreferencesMin, prepTimePreferencesMax = prepTimePreferences.split("-")

        filter["prep_time__gte"] = int(prepTimePreferencesMin)
        filter["prep_time__lte"] = int(prepTimePreferencesMax)

    if cookingMethodPreferences:
        filter["cooking_method"] = cookingMethodPreferences

    # if ingredientPreferences:
    #     filter["ingredients"] = ingredientPreferences


    queryset = Food.objects.filter(**filter)

    serializer = FoodSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

















    print(queryset)






