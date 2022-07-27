from django.urls import path
from .views import index, show_category

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index' ),
    path('categroy/<slug:slug>/', show_category, name='products_category')
]
