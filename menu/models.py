from django.db import models

# Create your models here.


## creating a class for food items

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name



class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="foods")

    def __str__(self):
        return self.name










   


