from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),






    path('category/<int:id>/', views.category_detail, name='category_detail'),


]
