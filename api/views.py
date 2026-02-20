from django.shortcuts import render
from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer
from django.contrib.postgres.search import SearchQuery
from django.db.models import Func, F


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

    if requestedOption != 'main_ingredients' and requestedOption != 'optional_ngredients':

      queryset =   Food.objects.values_list(requestedOption, flat=True).distinct()

    else: 

       queryset =  Food.objects.annotate(ingredient=Func(requestedOption), function="unnest").values_list(requestedOption, flat=True).distinct()



   

    


    print(queryset)

   




