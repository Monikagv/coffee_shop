from django.db import models


class InternationalSupplier(models.Model):
    """Model representing international coffee suppliers/markets"""
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.country})"
    
    class Meta:
        ordering = ['name']


class CoffeeBean(models.Model):
    """Model representing coffee beans from international market"""
    ROAST_CHOICES = [
        ('LIGHT', 'Light Roast'),
        ('MEDIUM', 'Medium Roast'),
        ('DARK', 'Dark Roast'),
    ]
    
    name = models.CharField(max_length=200)
    supplier = models.ForeignKey(InternationalSupplier, on_delete=models.CASCADE, related_name='coffee_beans')
    origin_country = models.CharField(max_length=100)
    roast_level = models.CharField(max_length=10, choices=ROAST_CHOICES, default='MEDIUM')
    description = models.TextField(blank=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.origin_country}"
    
    class Meta:
        ordering = ['name']


class ImportOrder(models.Model):
    """Model representing orders from international suppliers"""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    supplier = models.ForeignKey(InternationalSupplier, on_delete=models.CASCADE)
    coffee_bean = models.ForeignKey(CoffeeBean, on_delete=models.CASCADE)
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    order_date = models.DateTimeField(auto_now_add=True)
    expected_delivery = models.DateField(null=True, blank=True)
    actual_delivery = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.coffee_bean.name} from {self.supplier.name}"
    
    class Meta:
        ordering = ['-order_date']
