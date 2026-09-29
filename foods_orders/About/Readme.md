# 🛒 Django Food Ordering & Cart System

A simple **Food Ordering Web Application** built with Django.  
Users can browse categories (Tea, Cold Drinks, Snacks, etc.), view products, and add them directly to their cart.  
The project demonstrates Django fundamentals: Models, Views, Templates, Authentication, and Cart Management.

---

## 🚀 Features

-  Category Management -- Organize products into categories (Tea, Cold Drinks, Snacks, etc.).
- Product Listing -- Show products with images, names, and prices.
- Add to Cart -- Users can add products directly to their cart.
- Cart Detail Page -- Displays all items, quantities, and totals.
- Authentication -- Only logged-in users can add to cart.
- Responsive UI --  Built with Bootstrap for neat card layouts.

---

## 🛠️ Tech Stack

- Backend: Django (Python)  
- Frontend: HTML, CSS, Bootstrap  
- Database: SQLite 
- Authentication: Django’s built-in user system  

---

## 📂 Project Structure

foods_orders/
│
├── menu/                # Categories & Products
│   ├── models.py
│   ├── views.py
│   └── templates/menu/
│
├── orders/              # Cart functionality
│   ├── models.py
│   ├── views.py
│   └── templates/orders/
│       └── cart_detail.html
│
├── accounts/            # User authentication
│   ├── views.py
│   └── templates/accounts/
│
├── media/             #  Images
└── About/           # Text file



---

## ⚙️ Setup Instructions

1. Clone the repo
   ```bash
   git clone https://github.com/Saumya8805/foods_orders.git
   cd foods_orders
   --in terminal "python manage.py runserver"
   



