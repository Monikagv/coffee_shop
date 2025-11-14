from django.contrib import admin
from .models import Category, Coffee, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'size', 'price', 'is_available', 'created_at']
    list_filter = ['category', 'size', 'is_available']
    search_fields = ['name', 'description']
    list_editable = ['is_available', 'price']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['customer__username', 'notes']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'coffee', 'quantity', 'price']
    list_filter = ['order__status']
