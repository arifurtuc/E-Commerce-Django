# What is this project?

This is a Django project showcasing an e-commerce platform where users can search products, add products to their cart and place orders through a checkout form. The admin panel allows administrators to manage product categories, products, and user orders.

## Features

- **User Features:**
  - Search products by name
  - Add products to the cart
  - View cart contents
  - Checkout form for placing orders

- **Admin Features:**
  - Manage product categories
  - Manage products
  - Manage user orders

## Installation

1. Clone the repository.
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Django migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the Django development server:

    ```bash
    python manage.py runserver
    ```
