from django.urls import path
from . import views
from accounts.views import custom_logout

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    

    path('accounts/logout/', custom_logout, name='logout'),
]
