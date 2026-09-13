# ⚡ Sportify — Modern Sports Equipment & Accessories E-Commerce

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/rashijain-11/sportify)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/rashijain-11/sportify)

Sportify is a modern, responsive, and beginner-friendly e-commerce web application built using **Python and Django**. It allows users to browse sports gear across 8 popular sports categories, filter by price and sport, inspect high-resolution product details, select sizes/variants, manage a persistent shopping cart, checkout through a mock payment gateway, and manage user accounts with full order histories.

---

## 📁 Project Folder Structure

```
sportify/
│
├── manage.py                   # Command-line utility to run, migrate, and seed your project
├── db.sqlite3                  # The local SQLite database file
│
├── sportify/                   # Core project configuration package
│   ├── __init__.py             # Marks directory as a Python package
│   ├── settings.py             # Global settings (Installed apps, database, static/media, auth)
│   ├── urls.py                 # Main URL router directing traffic to each app
│   ├── context_processors.py   # Global variables (categories, cart badge count) for all pages
│   ├── asgi.py                 # ASGI configuration for async web servers
│   └── wsgi.py                 # WSGI configuration for production servers
│
├── products/                   # Catalog, Categories, Search, and Filtering
│   ├── models.py               # Category and Product database models
│   ├── views.py                # Logic for Homepage, Shop catalog, and Product detail pages
│   ├── urls.py                 # URL routes for products (/shop/, /product/<slug>/, etc.)
│   ├── admin.py                # Django admin configuration for products & categories
│   ├── tests.py                # Automated tests for catalog and products
│   └── management/
│       └── commands/
│           └── seed_data.py    # Custom command to populate 8 sports & 17+ products
│
├── orders/                     # Shopping Cart, Checkout, and Order Records
│   ├── models.py               # Cart, CartItem, Order, and OrderItem database models
│   ├── views.py                # Logic for cart (add, remove, update), checkout, order receipt
│   ├── urls.py                 # URL routes for cart and checkout (/cart/, /checkout/, etc.)
│   ├── utils.py                # Helper function to get/create cart for guest or user
│   ├── admin.py                # Django admin configuration for managing customer orders
│   └── tests.py                # Automated tests for cart and checkout
│
├── accounts/                   # User Authentication and Customer Profiles
│   ├── models.py               # UserProfile model storing shipping address & contact info
│   ├── forms.py                # User registration form and profile edit form
│   ├── views.py                # Signup, login, logout, and profile/order history logic
│   ├── urls.py                 # URL routes for auth (/accounts/login/, /signup/, etc.)
│   ├── admin.py                # User profile integrated into Django user admin
│   └── tests.py                # Automated tests for authentication
│
├── templates/                  # HTML Templates rendered by Django
│   ├── base.html               # Shared layout (Header, Navbar, Messages, Footer, Modals)
│   ├── products/
│   │   ├── home.html           # Homepage (Hero, 8 Categories, Featured Gear, Offer, Promise)
│   │   ├── shop.html           # Product catalog with sidebar filters, search & sorting
│   │   └── product_detail.html # Product page with variants, quantity picker, related items
│   ├── orders/
│   │   ├── cart.html           # Cart table with + / - quantity controls and price breakdown
│   │   ├── checkout.html       # Shipping form, order summary, and mock payment options
│   │   └── order_success.html  # Order confirmation receipt with order ID
│   └── accounts/
│       ├── login.html          # Clean branded login form
│       ├── signup.html         # User registration form
│       └── profile.html        # Athlete profile and previous orders dashboard
│
├── static/                     # Static files (Custom CSS, JS, brand images)
│   ├── css/
│   │   └── custom.css          # Premium sporty styling, custom colors, animations
│   ├── js/
│   │   └── main.js             # Interactive controls (quantity adjustments, payment toggles)
│   └── images/                 # Static brand assets
│
└── media/                      # Uploaded files (Product photos uploaded via Admin)
    ├── products/
    └── categories/
```

---

## 🚀 Beginner's Quick-Start Guide (Step-by-Step)

Follow these exact commands in your terminal (PowerShell or Command Prompt).

### Step 1: Open Terminal in the Project Directory
Navigate into the `sportify` directory:
```powershell
cd C:\Users\rashi\Desktop\sportify
```

### Step 2: Activate the Virtual Environment
A **virtual environment** is an isolated workspace that contains all the Python libraries for this project without affecting the rest of your computer.

On Windows PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```
*(If PowerShell shows an execution policy warning, you can run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once, or activate with `.\venv\Scripts\activate.bat`)*

When activated, you will see `(venv)` at the beginning of your terminal prompt!

### Step 3: Run Database Migrations
Migrations translate the Python model definitions in `models.py` into database tables inside `db.sqlite3`.
```powershell
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Populate Seed Data (Categories & Products)
We have included a pre-built data generator that loads 8 sports categories and 17 realistic items:
```powershell
python manage.py seed_data
```
> **Default Admin Account created by the seeder:**
> - **Username:** `admin`
> - **Password:** `admin123`

### Step 5: Start the Development Server
```powershell
python manage.py runserver
```

Now open your web browser and navigate to:
👉 **`http://127.0.0.1:8000/`**

To view the Django Admin panel:
👉 **`http://127.0.0.1:8000/admin/`** (Log in with `admin` / `admin123`)

---

## 🎨 Design & Palette

Sportify is styled using a modern athletic palette:
- **White** (`#ffffff`): Clean background and abundant whitespace
- **Light Blue** (`#e0f2fe`, `#f0f9ff`): Soft cards, badges, and icon backgrounds
- **Medium Blue** (`#0284c7`, `#0ea5e9`): Buttons, active navigation pills, primary highlights
- **Dark Navy Blue** (`#0f172a`, `#1e293b`): Hero banner, typography, and footer

---

## 🧪 Running Automated Tests

Run the built-in test suite to verify catalog queries, cart calculations, orders, and authentication:
```powershell
python manage.py test
```

---

## 🛠️ How to Customize

- **Add New Products or Categories:** Log into `http://127.0.0.1:8000/admin/` and click "+ Add" next to Products or Categories.
- **Edit Colors or CSS:** Open `static/css/custom.css` and adjust `:root` variables at the top.
- **Modify Layouts:** Open `templates/base.html` for header/footer, or `templates/products/home.html` for the homepage.
