from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from international_market.models import InternationalSupplier, CoffeeBean, ImportOrder
from shop.models import LocalCoffeeProduct, Inventory, Customer, LocalOrder, OrderItem


class Command(BaseCommand):
    help = 'Populates the database with sample data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')

        # Create International Suppliers
        suppliers_data = [
            {'name': 'Colombian Coffee Exports', 'country': 'Colombia', 'contact_email': 'contact@colombiancoffee.co', 'phone': '+57-1-234-5678'},
            {'name': 'Ethiopian Beans Co.', 'country': 'Ethiopia', 'contact_email': 'info@ethiopianbeans.et', 'phone': '+251-11-123-4567'},
            {'name': 'Brazilian Coffee Trade', 'country': 'Brazil', 'contact_email': 'sales@brazilcoffee.br', 'phone': '+55-11-9876-5432'},
            {'name': 'Vietnamese Coffee Export', 'country': 'Vietnam', 'contact_email': 'export@vietnamcoffee.vn', 'phone': '+84-24-3456-7890'},
        ]

        suppliers = []
        for data in suppliers_data:
            supplier, created = InternationalSupplier.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
            suppliers.append(supplier)
            if created:
                self.stdout.write(f'Created supplier: {supplier.name}')

        # Create Coffee Beans
        beans_data = [
            {'name': 'Colombian Supremo', 'supplier': suppliers[0], 'origin_country': 'Colombia', 'roast_level': 'MEDIUM', 
             'description': 'Rich and smooth with notes of caramel and nuts', 'price_per_kg': Decimal('28.50'), 'available_quantity_kg': Decimal('500')},
            {'name': 'Ethiopian Yirgacheffe', 'supplier': suppliers[1], 'origin_country': 'Ethiopia', 'roast_level': 'LIGHT',
             'description': 'Floral and fruity with bright acidity', 'price_per_kg': Decimal('32.00'), 'available_quantity_kg': Decimal('300')},
            {'name': 'Brazilian Santos', 'supplier': suppliers[2], 'origin_country': 'Brazil', 'roast_level': 'DARK',
             'description': 'Bold and chocolaty with low acidity', 'price_per_kg': Decimal('24.00'), 'available_quantity_kg': Decimal('800')},
            {'name': 'Vietnamese Robusta', 'supplier': suppliers[3], 'origin_country': 'Vietnam', 'roast_level': 'DARK',
             'description': 'Strong and earthy, perfect for espresso', 'price_per_kg': Decimal('18.50'), 'available_quantity_kg': Decimal('600')},
            {'name': 'Colombian Geisha', 'supplier': suppliers[0], 'origin_country': 'Colombia', 'roast_level': 'LIGHT',
             'description': 'Premium beans with jasmine and tropical fruit notes', 'price_per_kg': Decimal('65.00'), 'available_quantity_kg': Decimal('100')},
        ]

        beans = []
        for data in beans_data:
            bean, created = CoffeeBean.objects.get_or_create(
                name=data['name'],
                supplier=data['supplier'],
                defaults=data
            )
            beans.append(bean)
            if created:
                self.stdout.write(f'Created coffee bean: {bean.name}')

        # Create Import Orders
        orders_data = [
            {'supplier': suppliers[0], 'coffee_bean': beans[0], 'quantity_kg': Decimal('100'), 'total_cost': Decimal('2850.00'), 'status': 'DELIVERED'},
            {'supplier': suppliers[1], 'coffee_bean': beans[1], 'quantity_kg': Decimal('50'), 'total_cost': Decimal('1600.00'), 'status': 'SHIPPED'},
            {'supplier': suppliers[2], 'coffee_bean': beans[2], 'quantity_kg': Decimal('150'), 'total_cost': Decimal('3600.00'), 'status': 'DELIVERED'},
            {'supplier': suppliers[3], 'coffee_bean': beans[3], 'quantity_kg': Decimal('200'), 'total_cost': Decimal('3700.00'), 'status': 'CONFIRMED'},
        ]

        for data in orders_data:
            order, created = ImportOrder.objects.get_or_create(
                supplier=data['supplier'],
                coffee_bean=data['coffee_bean'],
                quantity_kg=data['quantity_kg'],
                defaults={
                    'total_cost': data['total_cost'],
                    'status': data['status'],
                    'expected_delivery': timezone.now().date() + timedelta(days=14)
                }
            )
            if created:
                self.stdout.write(f'Created import order: {order}')

        # Create Inventory entries
        for bean in beans[:4]:  # First 4 beans
            inv, created = Inventory.objects.get_or_create(
                coffee_bean=bean,
                defaults={
                    'current_stock_kg': Decimal('25.00'),
                    'minimum_stock_kg': Decimal('10.00')
                }
            )
            if created:
                self.stdout.write(f'Created inventory for: {bean.name}')

        # Create Local Coffee Products
        products_data = [
            {'name': 'Classic Espresso', 'product_type': 'ESPRESSO', 'source_bean': beans[3], 'price': Decimal('3.50')},
            {'name': 'Colombian Americano', 'product_type': 'AMERICANO', 'source_bean': beans[0], 'price': Decimal('4.00')},
            {'name': 'Ethiopian Cappuccino', 'product_type': 'CAPPUCCINO', 'source_bean': beans[1], 'price': Decimal('5.50')},
            {'name': 'Brazilian Latte', 'product_type': 'LATTE', 'source_bean': beans[2], 'price': Decimal('5.00')},
            {'name': 'Cold Brew Special', 'product_type': 'COLD_BREW', 'source_bean': beans[0], 'price': Decimal('6.00')},
            {'name': 'Colombian Supremo Beans (250g)', 'product_type': 'BEANS_RETAIL', 'source_bean': beans[0], 
             'description': 'Take home our premium Colombian beans', 'price': Decimal('12.50')},
            {'name': 'Ethiopian Yirgacheffe Beans (250g)', 'product_type': 'BEANS_RETAIL', 'source_bean': beans[1],
             'description': 'Premium Ethiopian beans for home brewing', 'price': Decimal('14.00')},
        ]

        products = []
        for data in products_data:
            product, created = LocalCoffeeProduct.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
            products.append(product)
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Create sample customers
        customers_data = [
            {'name': 'John Smith', 'email': 'john.smith@example.com', 'phone': '555-0101', 'loyalty_points': 150},
            {'name': 'Maria Garcia', 'email': 'maria.garcia@example.com', 'phone': '555-0102', 'loyalty_points': 230},
            {'name': 'David Chen', 'email': 'david.chen@example.com', 'phone': '555-0103', 'loyalty_points': 95},
        ]

        customers = []
        for data in customers_data:
            customer, created = Customer.objects.get_or_create(
                email=data['email'],
                defaults=data
            )
            customers.append(customer)
            if created:
                self.stdout.write(f'Created customer: {customer.name}')

        # Create sample orders
        if customers and products:
            order1, created = LocalOrder.objects.get_or_create(
                customer=customers[0],
                status='COMPLETED',
                defaults={'total_amount': Decimal('9.50')}
            )
            if created:
                OrderItem.objects.create(order=order1, product=products[0], quantity=1, price_at_purchase=products[0].price)
                OrderItem.objects.create(order=order1, product=products[4], quantity=1, price_at_purchase=products[4].price)
                self.stdout.write(f'Created order for {customers[0].name}')

            order2, created = LocalOrder.objects.get_or_create(
                customer=customers[1],
                status='PREPARING',
                defaults={'total_amount': Decimal('10.50')}
            )
            if created:
                OrderItem.objects.create(order=order2, product=products[2], quantity=2, price_at_purchase=products[2].price)
                self.stdout.write(f'Created order for {customers[1].name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated sample data!'))
