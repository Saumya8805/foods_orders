from django.db import models

# Create your models here.

## creating a class for food items
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name






    # menu/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='foods/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="foods")

