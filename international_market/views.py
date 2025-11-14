from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import InternationalSupplier, CoffeeBean, ImportOrder


def suppliers_dashboard(request):
    """Dashboard view for international suppliers"""
    suppliers = InternationalSupplier.objects.filter(is_active=True)
    recent_orders = ImportOrder.objects.all()[:5]
    context = {
        'suppliers': suppliers,
        'recent_orders': recent_orders,
    }
    return render(request, 'international_market/suppliers_dashboard.html', context)


class SupplierListView(ListView):
    model = InternationalSupplier
    template_name = 'international_market/supplier_list.html'
    context_object_name = 'suppliers'
    
    def get_queryset(self):
        return InternationalSupplier.objects.filter(is_active=True)


class CoffeeBeanListView(ListView):
    model = CoffeeBean
    template_name = 'international_market/coffeebean_list.html'
    context_object_name = 'coffee_beans'
    
    def get_queryset(self):
        return CoffeeBean.objects.filter(available_quantity_kg__gt=0)


class ImportOrderListView(ListView):
    model = ImportOrder
    template_name = 'international_market/importorder_list.html'
    context_object_name = 'orders'
    paginate_by = 20
