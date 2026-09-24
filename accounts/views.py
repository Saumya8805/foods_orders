
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout\



# Create your views here.

##view function for Signup form

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # after signup, go to login
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

#view function for logout

def custom_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')  

