from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catalog.views import show_products

urlpatterns = [
    path('', show_products, name='products_home'),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)