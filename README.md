# ⚡ Sportify — Modern Sports Equipment & Accessories E-Commerce

Sportify is a clean, responsive, and beginner-friendly e-commerce web application built using **Python + Django**, styled with **Bootstrap 5** and custom athletic CSS, and priced in **Indian Rupees (₹ / INR)**. It features a complete store catalog of 40 realistic products across 8 sports categories, dynamic search, price filtering, size/variant selection, a shopping cart, mock checkout with UPI/Card/COD, and customer order management.

---

## 🌐 Live Deployments & Cloud Links

Access the deployed application and 1-click cloud deployment blueprints:

- 🚀 **Vercel Live Website:** [Sportify — Premium Sports Equipment & Accessories](https://sportify-black.vercel.app/)
- ☁️ **Render 1-Click Deploy:** [Deploy on Render](https://render.com/deploy?repo=https://github.com/rashijain-11/sportify)
- 📊 **Render Cloud Dashboard:** [Render Management Dashboard](https://dashboard.render.com/)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/rashijain-11/sportify)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/rashijain-11/sportify)

---

## 📁 Project Structure & Architecture

Sportify follows a clean, modular Django architecture:

```
sportify/
│
├── manage.py                   # Django CLI tool to run the dev server, migrate, and seed data
├── db.sqlite3                  # Local SQLite database (persists categories, products, orders)
├── requirements.txt            # Python dependencies (Django, Pillow, Gunicorn, WhiteNoise)
├── render.yaml                 # Infrastructure blueprint for Render (Free tier, Singapore region)
├── vercel.json                 # Deployment configuration for Vercel serverless Python
├── build.sh                    # Build script for production deployments (installs packages & collects static)
│
├── sportify/                   # Core Project Settings
│   ├── settings.py             # App configuration, middleware, INR currency logic, static & media
│   ├── urls.py                 # Root URL router
│   ├── wsgi.py                 # WSGI production server entry point (Gunicorn & WhiteNoise)
│   └── context_processors.py   # Global context for navbar category dropdown and cart badge
│
├── products/                   # Storefront & Catalog Management
│   ├── models.py               # Category and Product models (prices, discounts, ratings, variants)
│   ├── views.py                # Homepage, Shop catalog (search, filter, sort, paginate), Product detail
│   ├── urls.py                 # Storefront routes (/, /shop/, /category/<slug>/, /product/<slug>/)
│   ├── admin.py                # Admin portal configuration to manage inventory
│   └── management/
│       └── commands/
│           └── seed_data.py    # Custom command to populate 8 categories and 40 products in ₹ (INR)
│
├── orders/                     # Shopping Cart & Checkout Flow
│   ├── models.py               # Cart, CartItem, Order, and OrderItem models
│   ├── views.py                # Cart detail, add/update/remove, checkout, and order confirmation
│   ├── urls.py                 # Routes for /cart/, /checkout/, and order receipts
│   └── utils.py                # Session-based cart helper supporting guest and logged-in users
│
├── accounts/                   # User Authentication & Profiles
│   ├── models.py               # UserProfile model (stores Indian delivery address & phone)
│   ├── views.py                # Login, signup, logout, and order history dashboard
│   └── urls.py                 # Auth routes (/accounts/login/, /accounts/signup/, /profile/)
│
├── templates/                  # HTML Templates (Bootstrap 5 + Custom CSS)
│   ├── base.html               # Master layout (Navbar, Notification Bar, Cart Badge, Footer, Modals)
│   ├── products/               # home.html, shop.html, product_detail.html
│   ├── orders/                 # cart.html, checkout.html, order_success.html
│   ├── accounts/               # login.html, signup.html, profile.html
│   ├── 404.html                # Friendly custom 404 Not Found error page
│   └── 500.html                # Friendly custom 500 Server Error page
│
└── static/                     # Static Assets
    ├── css/
    │   └── custom.css          # Sportify styling (White, Light Blue, Medium Blue, Dark Navy)
    └── js/
        └── main.js             # Interactive client-side logic (quantity selectors, payment toggles)
```

---

## 🚀 Quick-Start Guide (Local Development)

Follow these simple steps in your terminal (PowerShell or Command Prompt) to run Sportify locally:

### 1. Clone the Repository & Navigate to Directory
```powershell
git clone https://github.com/rashijain-11/sportify.git
cd sportify
```

### 2. Set Up and Activate Virtual Environment
```powershell
# Create virtual environment
python -m venv venv

# Activate on Windows PowerShell
.\venv\Scripts\Activate.ps1
```
*(If PowerShell restricts script execution, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once, or use Command Prompt with `venv\Scripts\activate.bat`)*

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Run Migrations & Populate Seed Catalog
```powershell
python manage.py migrate
python manage.py seed_data
```

> **Pre-configured Demo Admin Credentials:**
> - **Username:** `admin`
> - **Password:** `admin123`

### 5. Launch Development Server
```powershell
python manage.py runserver
```

Open your browser and visit:
- 🌐 **Storefront:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- ⚙️ **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🛍️ Features & Functional Modules

- **8 Sports Categories:** Cricket, Football, Basketball, Badminton, Tennis, Gym & Fitness, Running, and Sports Accessories.
- **40 Realistic Products:** Each seeded with high-definition sports photography, ratings, reviews, stock counts, size/variant choices, and Indian Rupee (₹) pricing.
- **Live Search & Price Filtering:** Instant keyword query search across titles and categories, with customizable min/max price sliders.
- **Sorting Options:** Sort items by newest arrivals, price (low to high), price (high to low), or customer ratings.
- **Persistent Shopping Cart:** Works seamlessly for both guest visitors and authenticated users with free shipping calculation over ₹999.
- **Mock Payment Checkout:** Simulates Credit/Debit Card, UPI / Net Banking, and Cash on Delivery (COD) orders with instant receipt generation.
- **User Dashboard:** Dedicated profile page showing order tracking, payment status, and saved Indian delivery addresses.
- **Fully Responsive Design:** Optimized for Desktop (3 cards/row), Tablet (2 cards/row), and Mobile (1 card/row).

---

## 🧪 Automated Testing

Sportify includes automated test suites covering catalog queries, cart calculations, order processing, and authentication:

```powershell
python manage.py test
```

To run the comprehensive full-site audit (validating all 40 products, categories, images, and routes):
```powershell
python audit.py
```

---

## 📄 License & Credits

Built with ❤️ for sports enthusiasts and athletes. Powered by **Python, Django, Bootstrap 5, and WhiteNoise**.
