from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid

class Cart(models.Model):
    """
    Shopping cart model that supports both logged-in users and anonymous session guests.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='carts')
    session_id = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user:
            return f"Cart of {self.user.username}"
        return f"Guest Cart ({self.session_id})"

    @property
    def get_subtotal(self):
        """Calculates cart subtotal before shipping."""
        return sum(item.get_total_price for item in self.items.all())

    @property
    def get_shipping(self):
        """Free shipping over ₹999, else ₹99 flat rate."""
        subtotal = self.get_subtotal
        if subtotal == 0 or subtotal >= 999:
            return 0.00
        return 99.00

    @property
    def get_total(self):
        """Calculates final total amount including shipping."""
        return float(self.get_subtotal) + float(self.get_shipping)

    @property
    def get_total_items(self):
        """Returns total quantity of items in cart."""
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    """
    An individual product line item inside a shopping cart.
    """
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=50, blank=True, default="Standard")

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.size})"

    @property
    def get_total_price(self):
        return self.product.current_price * self.quantity


class Order(models.Model):
    """
    Customer order record placed after checkout.
    """
    ORDER_STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    PAYMENT_CHOICES = [
        ('card', 'Mock Credit/Debit Card'),
        ('upi', 'Mock UPI / Net Banking'),
        ('cod', 'Cash on Delivery'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    order_number = models.CharField(max_length=50, unique=True, editable=False)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=25)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='card')
    payment_status = models.CharField(max_length=50, default='Paid')
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='Processing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = f"SPT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.order_number} - {self.full_name}"


class OrderItem(models.Model):
    """
    An individual item stored within a finalized order.
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=50, blank=True, default="Standard")

    def __str__(self):
        return f"{self.quantity} x {self.product_name}"

    @property
    def get_total_price(self):
        return self.price * self.quantity
