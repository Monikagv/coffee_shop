from django.contrib import admin
from .models import LocalCoffeeProduct, Inventory, Customer, LocalOrder, OrderItem


@admin.register(LocalCoffeeProduct)
class LocalCoffeeProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'source_bean', 'price', 'is_available']
    list_filter = ['product_type', 'is_available']
    search_fields = ['name', 'description']


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['coffee_bean', 'current_stock_kg', 'minimum_stock_kg', 'needs_restock', 'last_restocked']
    list_filter = ['coffee_bean']
    
    def needs_restock(self, obj):
        return obj.needs_restock()
    needs_restock.boolean = True


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'loyalty_points', 'created_at']
    search_fields = ['name', 'email', 'phone']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(LocalOrder)
class LocalOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'total_amount', 'order_date', 'completed_date']
    list_filter = ['status', 'order_date']
    search_fields = ['customer__name', 'customer__email']
    date_hierarchy = 'order_date'
    inlines = [OrderItemInline]
