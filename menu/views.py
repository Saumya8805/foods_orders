from django.shortcuts import render
from .models import FoodItem

# Create your views here.









def home(request):
    return render(request, 'menu/home.html')


def menu_list(request):
    items = FoodItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})


