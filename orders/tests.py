from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from products.models import Category, Product
from orders.models import Cart, CartItem, Order, OrderItem

class OrderAndCartTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Football")
        self.product = Product.objects.create(
            category=self.category,
            name="Pro Match Ball",
            description="Match ball",
            price=Decimal('1000.00'),
            stock=15
        )

    def test_cart_add_and_calculations(self):
        # 1. Add to cart
        response = self.client.post(
            reverse('cart_add', kwargs={'product_id': self.product.id}),
            {'quantity': 2, 'size': 'Size 5'}
        )
        self.assertEqual(response.status_code, 302)

        # 2. View cart
        cart_res = self.client.get(reverse('cart_detail'))
        self.assertEqual(cart_res.status_code, 200)
        self.assertContains(cart_res, "Pro Match Ball")
        self.assertContains(cart_res, "Size 5")

    def test_checkout_and_order_creation(self):
        # Add item to cart
        self.client.post(
            reverse('cart_add', kwargs={'product_id': self.product.id}),
            {'quantity': 2, 'size': 'Size 5'}
        )

        # Post checkout form
        checkout_data = {
            'full_name': 'Alex Morgan',
            'email': 'alex@example.com',
            'phone': '1234567890',
            'address': '45 Championship Road',
            'city': 'Portland',
            'state': 'OR',
            'postal_code': '97201',
            'payment_method': 'card'
        }
        response = self.client.post(reverse('checkout'), checkout_data)
        self.assertEqual(response.status_code, 302)

        order = Order.objects.first()
        self.assertIsNotNone(order)
        self.assertEqual(order.full_name, 'Alex Morgan')
        self.assertEqual(order.items.count(), 1)
        self.assertEqual(order.total_amount, Decimal('2000.00')) # 2 x 1000 = 2000 >= 999 => free shipping!

        # Check stock reduced from 15 to 13
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 13)
