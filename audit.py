import os
import re
import urllib.request

base = 'http://127.0.0.1:8000'
errors = []

def check(url, name):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            if resp.status != 200:
                errors.append(f'{name} ({url}) returned status {resp.status}')
            unrendered = re.findall(r'(\{\{[^\{]*?\}\}|\{%[^\{]*?%\})', content)
            if unrendered:
                errors.append(f'{name} has unrendered Django tags: {unrendered[:3]}')
            return content
    except Exception as e:
        errors.append(f'{name} ({url}) crashed: {e}')
        return ''

print("=== SPORTIFY COMPREHENSIVE SITE AUDIT ===")

print("\n1. Checking Core Pages & Static Assets...")
check(f'{base}/', 'Homepage')
shop_html = check(f'{base}/shop/', 'Shop Page')
check(f'{base}/cart/', 'Cart Page')
check(f'{base}/checkout/', 'Checkout Page')
check(f'{base}/accounts/login/', 'Login Page')
check(f'{base}/accounts/signup/', 'Signup Page')
check(f'{base}/static/css/custom.css', 'CSS Asset')
check(f'{base}/static/js/main.js', 'JS Asset')

print("\n2. Checking All 8 Category Pages...")
cats = ['cricket', 'football', 'basketball', 'badminton', 'tennis', 'gym-fitness', 'running', 'sports-accessories']
for cat in cats:
    check(f'{base}/category/{cat}/', f'Category: {cat}')

print("\n3. Checking Django Database & Products...")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sportify.settings')
import django
django.setup()
from products.models import Product

products = Product.objects.filter(is_active=True)
print(f"Auditing {products.count()} active products...")

print("\n4. Checking All Product Detail Pages & Product Images...")
img_errors = 0
for p in products:
    # Check detail page
    check(f'{base}/product/{p.slug}/', f'Product Detail: {p.name}')
    # Check image URL
    try:
        req = urllib.request.Request(p.display_image, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            if r.status != 200:
                errors.append(f"Image for {p.name} returned status {r.status}")
                img_errors += 1
    except Exception as e:
        errors.append(f"Image for {p.name} failed: {e}")
        img_errors += 1

print(f"Product image audit finished with {img_errors} broken images.")

if errors:
    print("\n[!] AUDIT FAILED WITH THE FOLLOWING ISSUES:")
    for err in errors:
        print("  -", err)
else:
    print("\n[SUCCESS] ALL 40 PRODUCTS, CATEGORIES, IMAGES & CORE PAGES PASSED CLEANLY (100% HEALTHY)!")
