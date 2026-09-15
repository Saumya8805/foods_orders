from django.shortcuts import render, redirect
from .models import CartItem
from menu.models import FoodItem

# Create your views here.

## define function for too add the food in our cart list


from django.contrib.auth.decorators import login_required



from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from menu.models import FoodItem

def add_to_cart(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        food_item=item
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')  

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'orders/cart.html', {'cart_items': cart_items})



##to increase or decrease the quantity of item

def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, user=request.user, food_item_id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()  # remove if quantity is 0
    return redirect('view_cart')



def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, user=request.user, food_item_id=item_id)
    cart_item.delete()
    return redirect('view_cart')



