from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('coffees/', views.CoffeeListView.as_view(), name='coffee_list'),
    path('coffee/<int:pk>/', views.CoffeeDetailView.as_view(), name='coffee_detail'),
]
