from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodItem

# Create your models here.

## this is the class for to add the item in our cart list   

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.food_item.name} (x{self.quantity})"
