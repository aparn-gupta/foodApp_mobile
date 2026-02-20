from django.contrib.postgres.fields import ArrayField
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=400)
    taste = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=100)
    main_ingredients = ArrayField(
            models.CharField(max_length=100),
            blank=True,
            default=list
        )
    optional_ingredients = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        default=list)
    recipe = models.CharField(max_length=2000, null=True)
    calories = models.IntegerField(null=True)
    prep_time = models.IntegerField(null=True)
    cooking_method = models.CharField(max_length=100, null=True)

    
    


    def __str__(self):
        return self.name
    


#  {
#     name: "Chickpea Spinach Curry",
#     taste: "spicy savory",
#     cookingMethod: "simmering",
#     mainIngredients: ["chickpeas", "spinach", "tomatoes", "onion", "garam masala"],
#     region: "Indian",
#     recipe: "Cooked chickpeas are simmered in a spiced tomato-onion base infused with garlic and garam masala. Fresh spinach is added toward the end and gently wilted into the curry. The dish is slow-cooked until thick and aromatic, making it perfect with rice or flatbread.",
#     calories: 320,
#     prepTime: 35,
#     optionalIngredients: ["coconut milk", "fresh coriander", "green chili"]
#   },



# Create your models here.
