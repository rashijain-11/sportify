from products.models import Category
from orders.utils import get_or_create_cart

def sportify_context(request):
    """
    Global context processor to make categories and cart items count
    available across all templates (e.g. navbar, footer).
    """
    categories = Category.objects.all()
    cart_count = 0
    try:
        cart = get_or_create_cart(request)
        cart_count = cart.get_total_items
    except Exception:
        cart_count = 0

    return {
        'nav_categories': categories,
        'cart_count': cart_count,
    }
