from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    raw_id_fields = ['product']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'session_id', 'get_total_items', 'get_total', 'created_at']
    inlines = [CartItemInline]
    readonly_fields = ['created_at', 'updated_at']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number',
        'full_name',
        'email',
        'phone',
        'total_amount',
        'payment_method',
        'payment_status',
        'order_status',
        'created_at'
    ]
    list_filter = ['order_status', 'payment_status', 'payment_method', 'created_at']
    search_fields = ['order_number', 'full_name', 'email', 'phone', 'city']
    list_editable = ['order_status', 'payment_status']
    inlines = [OrderItemInline]
    readonly_fields = ['order_number', 'created_at', 'updated_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_name', 'price', 'quantity', 'size', 'get_total_price']
    list_filter = ['order__created_at']
    search_fields = ['product_name', 'order__order_number']
