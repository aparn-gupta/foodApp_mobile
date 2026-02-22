from django.urls import path
from .views import AllFood, FoodDetails, options, loadDishes



urlpatterns = [
    path('list/',  AllFood.as_view(), name='all-food-list'),
    path('update/<int:id>/', FoodDetails.as_view(), name='food-details-update'),
    path('options/', options, name='options'  ),
    path('preferences/', loadDishes, name='preferences')

]