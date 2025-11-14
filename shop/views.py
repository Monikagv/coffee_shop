from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Coffee, Category, Order


def home(request):
    """Home page view"""
    categories = Category.objects.all()
    featured_coffees = Coffee.objects.filter(is_available=True)[:6]
    context = {
        'categories': categories,
        'featured_coffees': featured_coffees,
    }
    return render(request, 'shop/home.html', context)


class CoffeeListView(ListView):
    """List all available coffees"""
    model = Coffee
    template_name = 'shop/coffee_list.html'
    context_object_name = 'coffees'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Coffee.objects.filter(is_available=True)
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CoffeeDetailView(DetailView):
    """Detail view for a specific coffee"""
    model = Coffee
    template_name = 'shop/coffee_detail.html'
    context_object_name = 'coffee'


def menu(request):
    """Display the coffee menu by categories"""
    categories = Category.objects.prefetch_related('coffees').all()
    context = {
        'categories': categories,
    }
    return render(request, 'shop/menu.html', context)
