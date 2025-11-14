from django.db import models
from international_market.models import CoffeeBean


class LocalCoffeeProduct(models.Model):
    """Model representing coffee products produced locally from international beans"""
    PRODUCT_TYPE_CHOICES = [
        ('ESPRESSO', 'Espresso'),
        ('AMERICANO', 'Americano'),
        ('CAPPUCCINO', 'Cappuccino'),
        ('LATTE', 'Latte'),
        ('COLD_BREW', 'Cold Brew'),
        ('BEANS_RETAIL', 'Retail Coffee Beans'),
    ]
    
    name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
    source_bean = models.ForeignKey(CoffeeBean, on_delete=models.SET_NULL, null=True, blank=True, related_name='local_products')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - ${self.price}"
    
    class Meta:
        ordering = ['name']


class Inventory(models.Model):
    """Model for managing local coffee inventory"""
    coffee_bean = models.ForeignKey(CoffeeBean, on_delete=models.CASCADE)
    current_stock_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    minimum_stock_kg = models.DecimalField(max_digits=10, decimal_places=2, default=5)
    last_restocked = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.coffee_bean.name} - {self.current_stock_kg}kg in stock"
    
    def needs_restock(self):
        return self.current_stock_kg <= self.minimum_stock_kg
    
    class Meta:
        verbose_name_plural = "Inventories"


class Customer(models.Model):
    """Model representing coffee shop customers"""
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    loyalty_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.email})"
    
    class Meta:
        ordering = ['name']


class LocalOrder(models.Model):
    """Model representing customer orders at the local shop"""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PREPARING', 'Preparing'),
        ('READY', 'Ready'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(LocalCoffeeProduct, through='OrderItem')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        customer_name = self.customer.name if self.customer else "Walk-in"
        return f"Order #{self.id} - {customer_name}"
    
    class Meta:
        ordering = ['-order_date']


class OrderItem(models.Model):
    """Model representing items in a local order"""
    order = models.ForeignKey(LocalOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(LocalCoffeeProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_at_purchase = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Order #{self.order.id}"
    
    class Meta:
        unique_together = ['order', 'product']
