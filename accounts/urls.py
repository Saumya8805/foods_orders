from django.urls import path
from . import views
from accounts.views import custom_logout

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.signup, name='signup'),
    path('accounts/logout/', custom_logout, name='logout'),
   
]






