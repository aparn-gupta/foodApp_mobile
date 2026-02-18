from django.shortcuts import render
from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer


class AllFood(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
# Create your views here.


class FoodDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = "id"