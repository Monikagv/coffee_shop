# Coffee Shop - Django Practice Project

A Django web application for managing a coffee shop, built for practicing Django concepts.

## Features

- **Product Management**: Manage coffee products with categories, sizes, and prices
- **Admin Interface**: Full Django admin interface for managing the shop
- **Menu Display**: Browse coffee menu organized by categories
- **Product Listings**: View all available coffees with filtering
- **Order System**: Track customer orders and order items

## Models

- **Category**: Coffee categories (Espresso, Latte, Cappuccino, etc.)
- **Coffee**: Individual coffee products with name, description, price, size, and availability
- **Order**: Customer orders with status tracking
- **OrderItem**: Individual items within orders

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
python manage.py migrate
```

4. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ to view the site
7. Visit http://127.0.0.1:8000/admin/ to access the admin panel

## Usage

### Admin Interface
- Login to the admin panel at `/admin/`
- Add categories (e.g., Espresso, Latte, Cappuccino)
- Add coffee products with details
- Manage orders

### Customer Interface
- **Home**: View featured coffees
- **Menu**: Browse all coffees organized by category
- **Browse Coffees**: See all available coffees in a grid layout
- **Coffee Details**: View detailed information about each coffee

## Project Structure

```
coffee_shop/
├── coffee_shop_project/    # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/                   # Coffee shop app
│   ├── models.py          # Data models
│   ├── views.py           # Views
│   ├── admin.py           # Admin configuration
│   ├── urls.py            # URL patterns
│   └── templates/         # HTML templates
├── manage.py
└── requirements.txt
```

## Technologies Used

- Django 5.2.8
- Python 3.12
- SQLite (default database)
- Pillow (for image handling)

## Learning Objectives

This project demonstrates:
- Django project structure and setup
- Models and relationships (ForeignKey, related_name)
- Django admin customization
- Class-based views (ListView, DetailView)
- Function-based views
- URL routing
- Template inheritance and context
- Static file configuration
- Database migrations

## License

This is a practice project for learning Django.