from django.shortcuts import render
from .models import FoodItem
from django.shortcuts import render, get_object_or_404



# Create your views here.
def home(request):
    return render(request, 'menu/home.html')


def menu_list(request):
    items = FoodItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})





