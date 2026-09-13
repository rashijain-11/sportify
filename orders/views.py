from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from products.models import Product
from .models import Cart, CartItem, Order, OrderItem
from .utils import get_or_create_cart

def cart_detail(request):
    """
    Displays the shopping cart page with all added products,
    subtotal, shipping calculation, and checkout button.
    """
    cart = get_or_create_cart(request)
    context = {
        'cart': cart,
        'items': cart.items.select_related('product').all(),
    }
    return render(request, 'orders/cart.html', context)


def cart_add(request, product_id):
    """
    Adds a product to the cart with the selected size and quantity.
    Supports 'Add to Cart' and instant 'Buy Now'.
    """
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id, is_active=True)
        cart = get_or_create_cart(request)

        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity < 1:
                quantity = 1
        except ValueError:
            quantity = 1

        size = request.POST.get('size', 'Standard')

        # Check if item with exact product and size already exists in cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            size=size,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        messages.success(request, f"Added {product.name} ({size}) to your cart!")

        # Handle 'Buy Now' button click
        if request.POST.get('action') == 'buy_now':
            return redirect('checkout')

    return redirect('cart_detail')


def cart_update(request, item_id):
    """
    Updates the quantity of a specific cart item (+ / - or direct input).
    """
    if request.method == 'POST':
        cart = get_or_create_cart(request)
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        action = request.POST.get('action')

        if action == 'increase':
            if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity += 1
                cart_item.save()
            else:
                messages.warning(request, f"Maximum available stock for this item is {cart_item.product.stock}.")
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
                messages.info(request, "Item removed from cart.")

    return redirect('cart_detail')


def cart_remove(request, item_id):
    """
    Removes a single product item from the shopping cart.
    """
    cart = get_or_create_cart(request)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.info(request, f"Removed {product_name} from your cart.")
    return redirect('cart_detail')


def checkout(request):
    """
    Handles order checkout, shipping details capture,
    mock payment method selection, and order creation.
    """
    cart = get_or_create_cart(request)
    items = cart.items.select_related('product').all()

    if not items.exists():
        messages.warning(request, "Your cart is empty. Please add items to checkout.")
        return redirect('shop')

    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()
        city = request.POST.get('city', '').strip()
        state = request.POST.get('state', '').strip()
        postal_code = request.POST.get('postal_code', '').strip()
        payment_method = request.POST.get('payment_method', 'card')

        if not all([full_name, email, phone, address, city, state, postal_code]):
            messages.error(request, "Please fill in all required shipping fields.")
            return redirect('checkout')

        with transaction.atomic():
            # Create Order
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                full_name=full_name,
                email=email,
                phone=phone,
                address=address,
                city=city,
                state=state,
                postal_code=postal_code,
                subtotal=cart.get_subtotal,
                shipping=cart.get_shipping,
                total_amount=cart.get_total,
                payment_method=payment_method,
                payment_status='Paid' if payment_method in ['card', 'upi'] else 'Pending',
                order_status='Processing'
            )

            # Create OrderItems and reduce product stock
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    product_name=item.product.name,
                    price=item.product.current_price,
                    quantity=item.quantity,
                    size=item.size
                )
                if item.product.stock >= item.quantity:
                    item.product.stock -= item.quantity
                    item.product.save()

            # Clear cart items after successful order creation
            cart.items.all().delete()

            # Save address info to profile if user is authenticated
            if request.user.is_authenticated and hasattr(request.user, 'profile'):
                profile = request.user.profile
                if not profile.phone: profile.phone = phone
                if not profile.address: profile.address = address
                if not profile.city: profile.city = city
                if not profile.state: profile.state = state
                if not profile.postal_code: profile.postal_code = postal_code
                profile.save()

        messages.success(request, f"🎉 Success! Order #{order.order_number} placed successfully!")
        return redirect('order_success', order_number=order.order_number)

    # Initial data for logged in user
    initial_data = {}
    if request.user.is_authenticated:
        initial_data['full_name'] = f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username
        initial_data['email'] = request.user.email
        if hasattr(request.user, 'profile'):
            initial_data['phone'] = request.user.profile.phone
            initial_data['address'] = request.user.profile.address
            initial_data['city'] = request.user.profile.city
            initial_data['state'] = request.user.profile.state
            initial_data['postal_code'] = request.user.profile.postal_code

    context = {
        'cart': cart,
        'items': items,
        'initial': initial_data,
    }
    return render(request, 'orders/checkout.html', context)


def order_success(request, order_number):
    """
    Displays the order confirmation receipt page with order details and items.
    """
    order = get_object_or_404(Order, order_number=order_number)
    context = {
        'order': order,
    }
    return render(request, 'orders/order_success.html', context)
