from django.contrib import admin
from .models import FoodItem 

# Register your models here.



from django.contrib import admin
from .models import FoodItem, Category

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
