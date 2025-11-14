from django.urls import path
from . import views

app_name = 'international_market'

urlpatterns = [
    path('', views.suppliers_dashboard, name='dashboard'),
    path('suppliers/', views.SupplierListView.as_view(), name='supplier_list'),
    path('coffee-beans/', views.CoffeeBeanListView.as_view(), name='coffeebean_list'),
    path('import-orders/', views.ImportOrderListView.as_view(), name='importorder_list'),
]
