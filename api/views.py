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

      queryset =   Food.objects.values_list(requestedOption, flat=True).distinct()

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














    print(queryset)






