from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('category/<slug:category_slug>/', views.shop, name='shop_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]
