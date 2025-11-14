# Coffee Shop - International Market Connection

A Django-based coffee shop management system that connects to international coffee markets to source and produce coffee locally.

## Overview

This project represents a modern coffee shop that maintains direct relationships with international coffee suppliers from around the world. We source high-quality coffee beans from countries like Colombia, Ethiopia, Brazil, Vietnam, and others, then roast and process them locally to create fresh, artisan coffee products.

## Features

### International Market Integration
- **Supplier Management**: Connect with coffee suppliers worldwide
- **Coffee Bean Sourcing**: Browse and order premium coffee beans from international markets
- **Import Order Tracking**: Manage orders from international suppliers with status tracking
- **Multi-country Support**: Source beans from various coffee-producing regions

### Local Shop Operations
- **Product Management**: Create coffee products from internationally sourced beans
- **Inventory Control**: Track local inventory with automated restock alerts
- **Customer Management**: Manage customer information and loyalty points
- **Order Processing**: Handle local customer orders with status tracking
- **Menu Display**: Showcase products with origin information

## Project Structure

- `shop/` - Local coffee shop operations app
  - Models: LocalCoffeeProduct, Inventory, Customer, LocalOrder, OrderItem
  - Views and templates for customer-facing operations
  
- `international_market/` - International supplier connection app
  - Models: InternationalSupplier, CoffeeBean, ImportOrder
  - Dashboard for managing global supplier relationships

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Monikagv/coffee_shop.git
cd coffee_shop
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Access the application:
- Main site: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/
- International Market: http://localhost:8000/international/

## Usage

### Initial Setup via Admin Panel

1. Log in to the admin panel
2. Add International Suppliers (companies from coffee-producing countries)
3. Add Coffee Beans from these suppliers
4. Create Local Coffee Products using the beans
5. Set up Inventory entries for stock management
6. Add Customers (optional)
7. Process Orders through the shop

### Customer Experience

- Browse the menu to see products with their international origins
- View product details including source bean information
- See which country and supplier the coffee comes from
- Track order status

### Management Dashboard

- Monitor inventory levels with automatic low-stock alerts
- View international market dashboard
- Track import orders from suppliers
- Manage supplier relationships

## Models Overview

### International Market Models
- **InternationalSupplier**: Coffee suppliers from around the world
- **CoffeeBean**: Coffee beans available from suppliers
- **ImportOrder**: Orders placed with international suppliers

### Shop Models
- **LocalCoffeeProduct**: Coffee products produced locally
- **Inventory**: Stock management for coffee beans
- **Customer**: Customer information and loyalty tracking
- **LocalOrder**: Customer orders at the local shop
- **OrderItem**: Individual items in orders

## Technology Stack

- **Backend**: Django 5.2.8
- **Database**: SQLite (default, configurable)
- **Frontend**: Django Templates with custom CSS
- **Admin**: Django Admin interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for educational purposes.