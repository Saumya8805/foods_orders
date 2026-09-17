from django.shortcuts import render
from .models import FoodItem

# Create your views here.









def home(request):
    return render(request, 'menu/home.html')


def menu_list(request):
    items = FoodItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})


# menu/views.py
from django.shortcuts import render, get_object_or_404
from .models import Category

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.foods.all()
    return render(request, 'menu/category_detail.html', {
        'category': category,
        'products': products
    })
