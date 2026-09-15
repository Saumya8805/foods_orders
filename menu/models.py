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
