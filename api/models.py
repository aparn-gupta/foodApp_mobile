from django.contrib.postgres.fields import ArrayField
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=400)
    price = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    ingredients = ArrayField(
            models.CharField(max_length=100),
            blank=True,
            default=list
        )


    def __str__(self):
        return self.name



# Create your models here.
