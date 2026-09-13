from .models import Cart, CartItem

def get_or_create_cart(request):
    """
    Retrieves or creates the appropriate Cart for the current request.
    Handles both logged-in users and guest sessions, and seamlessly merges
    a guest cart into a user account when the user logs in.
    """
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    if request.user.is_authenticated:
        # Check if user already has a cart
        user_cart, _ = Cart.objects.get_or_create(user=request.user)

        # Check if there was an active guest cart during this session
        if session_key:
            guest_cart = Cart.objects.filter(session_id=session_key, user__isnull=True).first()
            if guest_cart and guest_cart != user_cart:
                # Merge guest items into user cart
                for g_item in guest_cart.items.all():
                    existing_item = user_cart.items.filter(
                        product=g_item.product,
                        size=g_item.size
                    ).first()
                    if existing_item:
                        existing_item.quantity += g_item.quantity
                        existing_item.save()
                    else:
                        g_item.cart = user_cart
                        g_item.save()
                guest_cart.delete()

        return user_cart
    else:
        # Guest user cart tied to session
        cart, _ = Cart.objects.get_or_create(session_id=session_key, user__isnull=True)
        return cart
