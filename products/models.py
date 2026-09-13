from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    """
    Model representing sports categories (e.g. Cricket, Football, Basketball).
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, help_text="Fallback image URL for demonstration")
    icon = models.CharField(max_length=50, default='bi-trophy', help_text="Bootstrap icon class name, e.g. bi-dribbble")

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop_by_category', kwargs={'category_slug': self.slug})

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return 'https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=600&auto=format&fit=crop&q=80'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model representing sports equipment and accessories.
    """
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Standard retail price")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Promotional discounted price if applicable")
    stock = models.PositiveIntegerField(default=20, help_text="Number of units in stock")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, help_text="Fallback image URL for demonstration")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.8)
    review_count = models.PositiveIntegerField(default=25)
    is_featured = models.BooleanField(default=False, help_text="Check to display on the homepage featured section")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide product from the store")
    sizes = models.CharField(max_length=150, blank=True, default="Standard", help_text="Comma-separated variants/sizes e.g. S, M, L, XL or Standard")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    @property
    def current_price(self):
        """Returns discount price if available, otherwise original price."""
        if self.discount_price and self.discount_price > 0:
            return self.discount_price
        return self.price

    @property
    def discount_percent(self):
        """Calculates discount percentage savings."""
        if self.discount_price and self.price > self.discount_price:
            discount = ((self.price - self.discount_price) / self.price) * 100
            return int(round(discount))
        return 0

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return 'https://images.unsplash.com/photo-1517649763962-0c623266ddc0?w=600&auto=format&fit=crop&q=80'

    @property
    def size_list(self):
        """Splits comma-separated sizes into a clean list."""
        if self.sizes:
            return [s.strip() for s in self.sizes.split(',') if s.strip()]
        return ['Standard']

    def __str__(self):
        return self.name
