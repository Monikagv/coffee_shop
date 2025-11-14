from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db import models
from .models import LocalCoffeeProduct, Inventory, Customer, LocalOrder


def home(request):
    """Home page view for the coffee shop"""
    available_products = LocalCoffeeProduct.objects.filter(is_available=True)
    recent_orders = LocalOrder.objects.all()[:5]
    low_stock_items = Inventory.objects.filter(current_stock_kg__lte=models.F('minimum_stock_kg'))
    
    context = {
        'products': available_products,
        'recent_orders': recent_orders,
        'low_stock_count': low_stock_items.count(),
    }
    return render(request, 'shop/home.html', context)


def menu(request):
    """Menu view showing all available products"""
    products = LocalCoffeeProduct.objects.filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'shop/menu.html', context)


class ProductListView(ListView):
    model = LocalCoffeeProduct
    template_name = 'shop/product_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return LocalCoffeeProduct.objects.filter(is_available=True)


class ProductDetailView(DetailView):
    model = LocalCoffeeProduct
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'


class OrderListView(ListView):
    model = LocalOrder
    template_name = 'shop/order_list.html'
    context_object_name = 'orders'
    paginate_by = 20


def inventory_status(request):
    """View to check inventory status"""
    all_inventory = Inventory.objects.all()
    low_stock = [inv for inv in all_inventory if inv.needs_restock()]
    
    context = {
        'all_inventory': all_inventory,
        'low_stock': low_stock,
    }
    return render(request, 'shop/inventory_status.html', context)
