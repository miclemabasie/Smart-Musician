from django.urls import path
from .views import show_category, show_product_detail

app_name = 'catalog'

urlpatterns = [
    path('categroy/<slug:slug>/', show_category, name='products_category'),
    path('products/<slug:slug>/', show_product_detail, name='products_details')
]
