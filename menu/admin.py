from django.contrib import admin
from .models import FoodItem 

# Register your models here.



@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'category')


