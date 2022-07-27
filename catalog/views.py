from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Category, Product


def index(request):
    page_title = 'Music instruments and sheet music for musicians'
    products = Product.objects.filter(is_active=True)

    template_name = 'home.html'
    context = {
        'user': request.user,
        'products': products
    }

    return render(request, template_name, context)

def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.product_set.all()
    print(category)
    template_name = 'catalog/products.html'
    context = {
        'category': category,
        'products': products,
    }

    return render(request, template_name, context)