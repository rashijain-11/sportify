from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Category, Product

def home(request):
    """
    Homepage view showing Hero banner, Sports categories,
    Featured products, Value propositions, and Special discount banner.
    """
    categories = Category.objects.all()
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:8]
    latest_deals = Product.objects.filter(discount_price__isnull=False, is_active=True)[:4]

    context = {
        'categories': categories,
        'featured_products': featured_products,
        'latest_deals': latest_deals,
    }
    return render(request, 'products/home.html', context)


def shop(request, category_slug=None):
    """
    Product listing page with search, category filtering,
    price filtering, and dynamic sorting.
    """
    products = Product.objects.filter(is_active=True)
    selected_category = None

    # 1. Filter by category slug from URL or GET parameter
    cat_param = category_slug or request.GET.get('category')
    if cat_param:
        selected_category = get_object_or_404(Category, slug=cat_param)
        products = products.filter(category=selected_category)

    # 2. Search query filter
    query = request.GET.get('q', '').strip()
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )

    # 3. Price range filtering
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        try:
            products = products.filter(price__gte=float(min_price))
        except ValueError:
            pass
    if max_price:
        try:
            products = products.filter(price__lte=float(max_price))
        except ValueError:
            pass

    # 4. Sorting
    sort_by = request.GET.get('sort', 'newest')
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    elif sort_by == 'rating':
        products = products.order_by('-rating', '-review_count')
    else:  # newest
        products = products.order_by('-created_at')

    # 5. Pagination (9 products per page)
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        'products': page_obj,
        'categories': categories,
        'selected_category': selected_category,
        'current_sort': sort_by,
        'search_query': query,
        'total_results': products.count(),
        'min_price': min_price or '',
        'max_price': max_price or '',
    }
    return render(request, 'products/shop.html', context)


def product_detail(request, slug):
    """
    Detailed single product page with high-res photo,
    variant/size selector, quantity selector, add to cart, and related items.
    """
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)
