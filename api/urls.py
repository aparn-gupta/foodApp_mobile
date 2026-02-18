from django.urls import path
from .views import AllFood, FoodDetails



urlpatterns = [
    path('list/',  AllFood.as_view(), name='all-food-list'),
    path('update/<int:id>/', FoodDetails.as_view(), name='food-details-update')
]