"""
URL configuration for sportify project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Interface
    path('admin/', admin.site.urls),

    # Storefront Apps
    path('', include('products.urls')),
    path('', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
]

# Serve media files uploaded by users/admin in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
