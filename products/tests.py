from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from products.models import Category, Product

class ProductCatalogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name="Cricket",
            description="All cricket equipment"
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Apex Pro Cricket Bat",
            description="Grade 1 willow bat",
            price=Decimal('100.00'),
            discount_price=Decimal('80.00'),
            stock=10,
            is_featured=True,
            sizes="Short Handle, Long Handle"
        )

    def test_category_slug_and_display(self):
        self.assertEqual(self.category.slug, "cricket")
        self.assertEqual(str(self.category), "Cricket")

    def test_product_properties(self):
        self.assertEqual(self.product.slug, "apex-pro-cricket-bat")
        self.assertEqual(self.product.current_price, Decimal('80.00'))
        self.assertEqual(self.product.discount_percent, 20)
        self.assertEqual(self.product.size_list, ["Short Handle", "Long Handle"])

    def test_home_page_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apex Pro Cricket Bat")
        self.assertContains(response, "Gear Up. Play Hard.")

    def test_shop_page_search_and_filter(self):
        response = self.client.get(reverse('shop'), {'q': 'cricket'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apex Pro Cricket Bat")

        # Category page
        response = self.client.get(reverse('shop_by_category', kwargs={'category_slug': 'cricket'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apex Pro Cricket Bat")

    def test_product_detail_page(self):
        response = self.client.get(reverse('product_detail', kwargs={'slug': 'apex-pro-cricket-bat'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Grade 1 willow bat")
