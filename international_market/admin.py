from django.contrib import admin
from .models import InternationalSupplier, CoffeeBean, ImportOrder


@admin.register(InternationalSupplier)
class InternationalSupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'contact_email', 'is_active', 'created_at']
    list_filter = ['is_active', 'country']
    search_fields = ['name', 'country', 'contact_email']


@admin.register(CoffeeBean)
class CoffeeBeanAdmin(admin.ModelAdmin):
    list_display = ['name', 'supplier', 'origin_country', 'roast_level', 'price_per_kg', 'available_quantity_kg']
    list_filter = ['roast_level', 'origin_country', 'supplier']
    search_fields = ['name', 'origin_country', 'description']


@admin.register(ImportOrder)
class ImportOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'supplier', 'coffee_bean', 'quantity_kg', 'total_cost', 'status', 'order_date']
    list_filter = ['status', 'order_date', 'supplier']
    search_fields = ['supplier__name', 'coffee_bean__name']
    date_hierarchy = 'order_date'
