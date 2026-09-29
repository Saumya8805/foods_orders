from django.shortcuts import render
from .models import FoodItem
from django.shortcuts import render, get_object_or_404
from .models import Category


# Create your views here.



def menu_list(request):
    items = FoodItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})



def home(request):
    categories = Category.objects.all()
    return render(request, 'menu/home.html', {'categories': categories})




def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.foods.all()
    return render(request, 'menu/category_detail.html', {
        'category': category,
        'products': products
    })






